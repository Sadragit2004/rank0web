from django.shortcuts import render
import web.settings as sett
from apps.company.models import MetaTag

# Create your views here.

def media_admin(request):


    context = {
        'media_url':sett.MEDIA_URL
    }

    return context




def main(request):

    meta = MetaTag.objects.filter(id = 1).first()
    return render(request,'main_app/main.html',{'meta':meta})