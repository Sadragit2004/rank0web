from django.shortcuts import render
from django.views import View
from apps.service.models import Plan
from .form import SearchForm


class Search(View):

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        context = {'form': form}
        return render(request, 'search_app/search.html', context)

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            price1 = data['price1']
            price2 = data['price2']

            # تبدیل قیمت‌های ذخیره‌شده به مقدار عددی
            plans = Plan.objects.filter(
                price__gte=price1,
                price__lte=price2
            )


        context = {
            'form': form,
            'plans': plans
        }
        return render(request, 'search_app/search.html', context)
