from django.shortcuts import render,redirect
from .models import MetaTag,Company, MainInfo,FAQ,WhyUs,why_us_2,SocialMedia,text_seo,Comm
from django.views import View
from django.contrib import messages

# Helper function to retrieve active companies
def get_active_companies():
    """
    Retrieves all active companies from the database.

    Returns:
        QuerySet: Active companies.
    """
    return Company.objects.filter(is_active=True)


def name_company(request):

    company = get_active_companies()

    return render(request,'company_app/detail_info/name_company.html',{'company':company})


def mobile_number(request):
    """
    Renders the mobile number page for active companies.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page for mobile numbers.
    """
    company_infos = get_active_companies()
    return render(request, 'company_app/detail_info/mobile_number.html', {'companys': company_infos})


def mobile_number2(request):
    """
    Renders the alternate mobile number page for active companies.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page for alternate mobile numbers.
    """
    company_infos = get_active_companies()
    return render(request, 'company_app/detail_info/mobile_number2.html', {'companys': company_infos})


def address(request):
    """
    Renders the address page for active companies.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page for addresses.
    """
    company_infos = get_active_companies()
    return render(request, 'company_app/detail_info/address.html', {'companys': company_infos})


def logo(request):
    """
    Renders the logo page for active companies.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page for logos.
    """
    company_infos = get_active_companies()
    return render(request, 'company_app/detail_info/logo.html', {'companys': company_infos})


def main_one(request):
    """
    Renders the main information page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page for main information.
    """

    main_page = MainInfo.objects.filter(is_active=True)
    return render(request, 'company_app/company.html', {'main_pages': main_page})


def Question(request):

    qus = FAQ.objects.filter(is_active = True).order_by('register_date')
    return render(request,'company_app/fqus.html',{'qus':qus})




def ShowWhyUS(request):

    why_us = WhyUs.objects.filter(is_active = True).order_by('-register_date')
    why_us2 = why_us_2.objects.filter(is_active = True).order_by('-register_date')
    return render(request,'company_app/why_us.html',{'whys':why_us,'why_us2':why_us2})





def ShowSocialMedia(request):

    social = SocialMedia.objects.filter(is_active = True).order_by('-created_at')
    return render(request,'company_app/detail_info/socialMediList.html',{'socials':social})



def show_meta(request):

    metas = MetaTag.objects.all()
    return render(request,'company_app/detail_info/meta_tags.html',{'meta_tags':metas})
    

def show_seo(request):

    text_seo1 = text_seo.objects.all()
    return render(request,'company_app/detail_info/text_seo.html',{'text_seo':text_seo1})
    

def show_comm(request):

    text_seo1 = Comm.objects.all()
    return render(request,'company_app/why_us.html',{'Comm':text_seo1})
    

from .form import CustomerForm
from .models import Customer


class CustomerCreateView(View):
    template_name = 'company_app/customer_form.html'

    def get(self, request):
        form = CustomerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'مشاورین ما بعد از ساعتی با شما تماس خواهند گرفت')
            return redirect('company:customer_create')  # باید در urls تعریف شود
        return render(request, self.template_name, {'form': form})