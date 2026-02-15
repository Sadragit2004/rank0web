from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Service,Groups,Meta_tag_model,Meta_tag_model_group


# Create your views here.

class ListService(View):

    def get(self,request,*args, **kwargs):

        service = Service.objects.filter(is_active = True).order_by('-created_at')
        return render(request,'service_app/list_service.html',{'services':service})




class ServiceDetail(View):

    def get(self,request,slug,*args, **kwargs):

        service = get_object_or_404(Service,slug = slug)

        meta_tags = Meta_tag_model.objects.filter(service = service).first()

        return render(request,'service_app/DetailService.html',{'service':service,'meta':meta_tags})


class ServiceDetailurl(View):

    def get(self,request,slug,*args, **kwargs):

        service = get_object_or_404(Service,slug = slug)

        meta_tags = Meta_tag_model.objects.filter(service = service).first()

        return render(request,'service_app/DetailService.html',{'service':service,'meta':meta_tags})




class ServiceDetailUrl(View):

    def get(self,request,slug,*args, **kwargs):

        service = get_object_or_404(Service,slug = slug)

        meta_tags = Meta_tag_model.objects.filter(service = service).first()

        return render(request,'service_app/DetailService.html',{'service':service,'meta':meta_tags})



def ShowMainService(request):

    services = Service.objects.filter(is_active = True).order_by('-created_at')
    return render(request,'service_app/service_main.html',{'services':services})





def ServiceGroups(request):

    groups = Groups.objects.filter(is_active = True).order_by('-created_at')
    return render(request,'service_app/groupsService.html',{'groups':groups})




def ShowServiceBygroup(request,*args, **kwargs):


    slug = kwargs['slug']
    groups = Groups.objects.filter(slug = slug).first()
    services = Service.objects.filter(groups = groups).order_by('-created_at')
    metas = Meta_tag_model_group.objects.filter(group_service = groups).first()

  
    return render(request,'service_app/serviceBygroup.html',{'services':services,'group':groups,'meta':metas})



def ReturnTitileService(request):

    titles = Service.objects.filter(is_active = True).order_by('-created_at')[:6]
    return render(request,'service_app/footer_titles.html',{'services':titles})