from django.urls import path
from .views import Search



app_name = 'search'

urlpatterns = [


    path('search/',Search.as_view(),name='search'),
    


]