from django.urls import path
from .views import ViewCall


app_name = 'call'

urlpatterns = [


    path('call',ViewCall.as_view(),name='call')


]