from django.urls import path
from .views import ShowBasicPlan,ShowListService,CollaborationView,Resum_CompanyView,show_member
app_name = 'whyus'

urlpatterns = [

    path('coll_view/',CollaborationView.as_view(),name='coll'),
    path('resum_company/',Resum_CompanyView.as_view(),name='resum'),
    path('members/',show_member,name='members'),
    path('service_list/',ShowListService,name='show_list'),
    path('show_basicPlan/',ShowBasicPlan,name='show_plan_basic'),



]