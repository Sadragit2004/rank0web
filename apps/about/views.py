from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import AboutUs, MetaTagModel

def get_active_companies():
    """
    Retrieves all active 'About Us' entries from the database.

    Returns:
        QuerySet: Active 'About Us' entries.
    """
    return AboutUs.objects.filter(is_active=True)

class AboutUsView(View):
    """
    Handles GET requests to display the 'About Us' page.
    """

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests for the 'About Us' page.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Rendered HTML page for 'About Us'.
        """
        abouts = get_active_companies()
        return render(request, 'about_app/about.html', {'abouts': abouts})

class ShowMetaView(ListView):
    """
    Displays a list of meta tags.
    """
    model = MetaTagModel
    template_name = 'about_app/meta_tags.html'
    context_object_name = 'meta_tags'


class englishabout(View):
  

    def get(self, request, *args, **kwargs):
       
        return render(request, 'about_app/profile.html')
