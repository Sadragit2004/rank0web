from django.shortcuts import render
from .models import PlanItem,Plan,Collaboration,Resum_company,Member_Company,ServiceList
from django.views import View
# Create your views here.


class CollaborationView(View):

    def get(self,request,*args, **kwargs):

        cobs = Collaboration.objects.filter(is_active = True).order_by('-created_at')
        return render(request,'whyUS_app/collabora.html',{'cobs':cobs})



class Resum_CompanyView(View):

    def get(self,request,*args, **kwargs):


        resums = Resum_company.objects.filter(is_active = True).order_by('-created_at')
        return render(request,'whyUS_app/resum_company.html',{'resums':resums})



def show_member(request):

    members = Member_Company.objects.filter(is_active = True).order_by('-created_at')
    return render(request,'whyUS_app/members.html',{'members':members})



def ShowListService(request):

    list_ser = ServiceList.objects.filter(is_active = True).order_by('-created_at')
    return render(request,'whyUS_app/list_service.html',{'services':list_ser})




def ShowBasicPlan(request):

    plans = Plan.objects.filter(is_active = True).order_by('created_at')
    return render(request,'whyUS_app/basicPlan22.html',{'plans':plans})

