from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [

    path('page',chat_page,name='chat_page'),
    path('send/', send_message, name='send_message'),
    path('messages/', get_messages, name='get_messages'),
    path('chat-panel/', admin_chat_dashboard, name='admin_chat_dashboard'),
    path('api/unseen-data/', unseen_data, name='unseen-data'),
    path('api/messages/', api_messages, name='api_messages'),

]

