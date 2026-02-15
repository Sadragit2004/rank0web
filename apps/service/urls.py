from django.urls import path
from .views import ServiceDetailurl,ReturnTitileService,ListService,ServiceDetail,ShowMainService,ServiceGroups,ShowServiceBygroup



app_name = 'service'

urlpatterns = [

    path('service/',ListService.as_view(),name='services'),
    path('service/<str:slug>',ServiceDetail.as_view(),name='detail_service'),
    path('service_main',ShowMainService,name='show_main_service'),
    path('serviceGroups/',ServiceGroups,name='service_group'),
    path('service/<str:slug>/',ShowServiceBygroup,name='by_group'),
    path('<str:slug>/',ServiceDetailurl.as_view(),name='www'),
    path('s/footer-title/',ReturnTitileService,name='titles_footer')

]