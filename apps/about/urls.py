from django.urls import path
from .views import englishabout,AboutUsView, ShowMetaView  # اصلاح ایمپورت

app_name = 'about'

urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about'),
    path('profile/sadra-abadkar', englishabout.as_view(), name='about'),
    path('meta-tags/', ShowMetaView.as_view(), name='show_meta')  # تغییر تابع به کلاس
]
