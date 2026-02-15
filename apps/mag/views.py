from django.shortcuts import render,get_object_or_404,redirect
from .models import main_tag_mag,SocialMediaAuthor,MagMainSlider,Mag,GroupMagModel,MetaTagModel,AuthorMagModel,Comment,MetaTagModelGroup
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Count
from django.views import View

# Create your views here.
def main(request):

    main_tag = main_tag_mag.objects.filter(id = 1).first()
    return render(request,'mag_app/mag_partial/main.html',{'meta':main_tag})



def show_slider(request):

    slider = MagMainSlider.objects.filter(is_active = True)
    return render(request,'mag_app/main_app/slider.html',{'slider':slider})


def MagsView(request):
    mags_list = Mag.objects.filter(is_active=True).order_by('-create_at')

    # دریافت شماره صفحه از URL
    page_number = request.GET.get('page', 1)

    # تعداد آیتم‌ها در هر صفحه (قابل تغییر)
    paginator = Paginator(mags_list, 6)

    mags = paginator.get_page(page_number)

    return render(request, 'mag_app/main_app/list_mag_main.html', {'mags': mags})
    
    
def MagsViewAll(request):
    mags_list = Mag.objects.filter(is_active=True).order_by('-create_at')

    # دریافت شماره صفحه از URL
    page_number = request.GET.get('page', 1)

    # تعداد آیتم‌ها در هر صفحه (قابل تغییر)
    paginator = Paginator(mags_list, 20)

    mags = paginator.get_page(page_number)

    return render(request, 'mag_app/main_app/all_mag.html', {'mags': mags})
    
    
def MagsViewBlogMain(request):
    # مقالات غیر تبلیغاتی
    mags_list = Mag.objects.filter(
        is_active=True
    ).exclude(
        group__slug='advertisement'
    ).order_by('-create_at')[:3]

    # مقالات تبلیغاتی
    ads_list = Mag.objects.filter(
        is_active=True,
        group__slug='advertisement'
    ).order_by('-create_at')[:3]  # می‌تونی [:3] رو برداری اگه می‌خوای همه بیان

    return render(request, 'blog_app/blog_main.html', {
        'blogs': mags_list,
        'ads': ads_list
    })


def show_best_Author(request):
    # واکشی نویسنده‌ای که بیشترین مقاله را دارد
    top_authors = AuthorMagModel.objects.annotate(num_articles=Count('mag')).order_by('-num_articles')
    max_articles = top_authors.first().num_articles if top_authors.exists() else 0
    top_authors = top_authors.filter(num_articles=max_articles).prefetch_related('socialmediaauthor')  # واکشی شبکه‌های اجتماعی

    context = {
        'top_authors': top_authors
    }

    return render(request, 'mag_app/main_app/best_authors.html', context)



def ExplorerMagView(request):

    mags = Mag.objects.filter(is_active = True).order_by('-view')[:5]

    return render(request,'mag_app/main_app/explorermags.html',{'mags':mags})


def top_parent_groups(request):
    groups = (
        GroupMagModel.objects
        .filter(is_active=True)
        .annotate(subgroup_count=Count('parent_of_group'))
        .order_by('-subgroup_count')[:5]
    )

    advertisement_articles = None
    for group in groups:
        if group.slug == "advertisement":
            advertisement_articles = Mag.objects.filter(group=group, is_active=True)

    return render(request, 'mag_app/main_app/top_groups.html', {
        'groups': groups,
        'advertisement_articles': advertisement_articles
    })


def group_list_view(request):
    groups = GroupMagModel.objects.filter(parent_group__isnull=True, is_active=True)

    # شناسایی گروه advertisement
    advertisement_group = groups.filter(slug='advertisement').first()
    advertisement_articles = None

    if advertisement_group:
        advertisement_articles = advertisement_group.magazines.filter(is_active=True)

    context = {
        'groups': groups,
        'advertisement_group': advertisement_group,
        'advertisement_articles': advertisement_articles,
    }
    return render(request, 'mag_app/main_app/header_group.html', context)


from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

class ShowByGroup(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        group = get_object_or_404(GroupMagModel, slug=slug)
        mags = group.magazines.all()

        page_number = request.GET.get('page', 1)
        paginator = Paginator(mags, 6)
        mags = paginator.get_page(page_number)
        meta = MetaTagModelGroup.objects.filter(group=group).first()

        # حذف کامل ?page=... از URL
        parsed_url = urlparse(request.build_absolute_uri())
        query_params = parse_qs(parsed_url.query)

        if 'page' in query_params:
            del query_params['page']  # حذف کامل page با هر مقداری

        new_query = urlencode(query_params, doseq=True)
        canonical_url = urlunparse((
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            new_query,
            parsed_url.fragment
        ))

        return render(request, 'mag_app/main_app/group_mag.html', {
            'group': group,
            'mags': mags,
            'meta': meta,
            'canonical_url': canonical_url,
        })

class MagDetailView(View):
    def get(self, request, group_slug, slug):
        group = get_object_or_404(GroupMagModel, slug=group_slug)  # دریافت گروه والد
        mag = get_object_or_404(Mag, slug=slug, group=group)  # مقاله فقط در این گروه جستجو شود
        comments = mag.comments.filter(parent__isnull=True)
        meta = MetaTagModel.objects.filter(blog=mag).first()
        return render(request, 'mag_app/main_app/magDetail.html', {'mag': mag, 'comments': comments, 'group': group,'meta':meta})

    def post(self, request, group_slug, slug):
        group = get_object_or_404(GroupMagModel, slug=group_slug)
        mag = get_object_or_404(Mag, slug=slug, group=group)
        author = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("text")
        parent_id = request.POST.get("parent_id")

        parent = None
        if parent_id:
            parent = get_object_or_404(Comment, id=parent_id)

        Comment.objects.create(mag=mag, author=author, email=email, text=text, parent=parent)
        return redirect("mag:show_detail_group", group_slug=group.slug, slug=mag.slug)




def search_view(request):
    query = request.GET.get('q', '')


    query = query.replace('ممد', '').strip()
    mags = Mag.objects.search_mag(query) if query else Mag.objects.none()

    page_number = request.GET.get('page', 1)

    # تعداد آیتم‌ها در هر صفحه (قابل تغییر)
    paginator = Paginator(mags, 6)

    mags = paginator.get_page(page_number)

    return render(request, 'mag_app/main_app/search.html', {'mags': mags})






def top_parent_groups_title(request):
    groups = (
        GroupMagModel.objects
        .filter(is_active=True)
        .annotate(subgroup_count=Count('parent_of_group'))
        .order_by('-subgroup_count')[:5]  # 5 گروه برتر که بیشترین زیرمجموعه دارند
    )
    return render(request, 'mag_app/main_app/footer_title.html', {'groups': groups})





def show_meta_main(request):

    metas = main_tag_mag.objects.all()
    return render(request,'mag_app/main_app/meta.html',{'metas':metas})
    
    
    
def MagTitleList(request):
    # مقالات غیر تبلیغاتی
    mags_list = Mag.objects.filter(
        is_active=True
    ).exclude(
        group__slug='advertisement'
    ).order_by('-create_at')[:6]

    # مقالات تبلیغاتی
    ads_list = Mag.objects.filter(
        is_active=True,
        group__slug='advertisement'
    ).order_by('-create_at')[:6]

    return render(request, 'mag_app/main_app/footer_mag.html', {
        'mags': mags_list,
        'ads': ads_list
    })
    
    
    
def MagAdsList(request):
    ads_list = Mag.objects.filter(
        is_active=True,
        group__slug='advertisement'
    ).order_by('-create_at')[:6]

    return render(request, 'mag_app/main_app/footer_ads_mag.html', {
        'ads': ads_list
    })

