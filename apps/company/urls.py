from django.urls import path
from .views import CustomerCreateView,show_seo,show_meta,ShowSocialMedia,name_company,main_one,mobile_number,address,mobile_number2,logo,Question,ShowWhyUS,show_comm

app_name = 'company'

urlpatterns = [

    path('mobile_number/',mobile_number,name='mobile_number'),
    path('mobile_number2/',mobile_number2,name='mobile_number2'),
    path('address/',address,name='address'),
    path('logo/',logo,name='logo'),
    path('main_one/',main_one,name='main_one'),
    path('qus/',Question,name='qustion'),
    path('why-us/',ShowWhyUS,name='show-why'),
    path('name-company/',name_company,name='name'),
    path('social-media',ShowSocialMedia,name='show_media'),
    path('show_seos',show_seo,name='seos'),
    path('Comm',show_comm,name='show_comm'),
    path('meta_tag/',show_meta,name='show_meta'),
    path('landing/customer/', CustomerCreateView.as_view(), name='customer_create'),
    



]