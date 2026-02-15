from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Q

from .models import Sample, Item, Feature, GallerySiteSample, Meta_tag_model,GroupSample,MetaTagModelGroup


class SampleView(View):
    def get(self, request, *args, **kwargs):
        samples = Sample.objects.filter(is_active=True).order_by('-created_at')
        return render(request, 'sample_app/list_sample1.html', {'samples': samples})


class SampleByGroup(View):
    def get(self, request, slug, *args, **kwargs):
        group = GroupSample.objects.filter(slug=slug).first()
        samples = Sample.objects.filter(group_sample=group).order_by('-created_at')
        meta = MetaTagModelGroup.objects.filter(group_sample=group).first()

        context = {
            'samples': samples,
            'slug': group.title_group if group else '',
            'meta': meta
        }
        return render(request, 'sample_app/sampleBygroup.html', context)


class SampleViewDetail(View):
    def get(self, request, slug, *args, **kwargs):
        sample = get_object_or_404(Sample, slug=slug)

        items = sample.sample_item.filter(is_active=True)
        features = sample.sample_feature.filter(is_active=True)
        gallery_images = sample.sample_Gallery.filter(is_active=True)
        meta_tags = Meta_tag_model.objects.filter(Sample_model=sample).first()

        context = {
            'sample': sample,
            'items': items,
            'features': features,
            'gallery_images': gallery_images,
            'meta': meta_tags,
        }

        return render(request, 'sample_app/DetailSample.html', context)


def show_main_sample(request):
    samples = Sample.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'sample_app/samples_main.html', {'samples': samples})


def show_groups(request):
    groups = GroupSample.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'sample_app/sample_groups.html', {'groups': groups})


def show_title_sample(request):
    samples = Sample.objects.filter(is_active=True).order_by('-created_at')[:6]
    return render(request, 'sample_app/sample_footer.html', {'samples': samples})
