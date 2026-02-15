from django.urls import path
from .views import SampleView,SampleViewDetail,show_main_sample,show_groups,SampleByGroup,show_title_sample


app_name = 'sample'

urlpatterns = [

    path('samples',SampleView.as_view(),name='sample_list'),
    path('sample-detail/<str:slug>/',SampleViewDetail.as_view(),name='detail_sample'),
    path('ShowSampleMain',show_main_sample,name='show_sample'),
    path('Groups',show_groups,name='show_groups'),
    path('samples/<str:slug>/',SampleByGroup.as_view(),name='sample_groups'),
    path('sample-footer/',show_title_sample,name='show_title')

]

