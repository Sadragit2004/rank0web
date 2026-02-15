# from django.shortcuts import render,redirect
# from django.views import View
# from .models import TypeCall,Call
# from .form import CallForm
# from django.contrib import messages


# # Create your views here.



# class ViewCall(View):

#     def get(self,request,*args, **kwargs):

#         form = CallForm()
#         return render(request,'call_app/call.html',{'form':form})


#     def post(self,request,*args, **kwargs):

#         form = CallForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             calls = Call.objects.create(

#                 type_call = data['type_call'],
#                 phone_number = data['phone_number'],
#                 title_time = data['title_time'],


#             )

#             messages.success(request,'درخواست شما با موفقیت ثبت شد در زمان تعیینی خود تماس گرفته خواهد شد','success')
#             return redirect('main:index')

#         else:
#             return render(request,'call_app/call.html',{'form':form})
"""Views for call management system."""

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Call
from .form import CallForm


class ViewCall(View):
    """مدیریت درخواست‌های تماس از طریق فرم."""

    def get(self, request, *args, **kwargs):
        """دریافت و نمایش فرم تماس."""
        form = CallForm()
        return render(request, 'call_app/call.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """دریافت و پردازش داده‌های فرم تماس."""
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()  # فرم ذخیره می‌شود، نیازی به `Call.objects.create` نیست.
            messages.success(request, 'درخواست شما با موفقیت ثبت شد و در زمان تعیین‌شده تماس گرفته خواهد شد.')
            return redirect('main:index')

        return render(request, 'call_app/call.html', {'form': form})



