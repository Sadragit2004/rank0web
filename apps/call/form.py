"""Forms for call management system."""

from django import forms
from .models import Call


class CallForm(forms.ModelForm):
    """فرم ثبت درخواست تماس."""

    class Meta:
        model = Call
        fields = ['type_call', 'phone_number', 'title_time', 'link_city']
        widgets = {
            'type_call': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'شماره تلفن',
                    'required': True,
                }
            ),
            'title_time': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'زمان تماس - مثلا 2 شب',
                    'required': True,
                }
            ),
            'link_city': forms.Textarea(  # اضافه کردن ویجت برای لینک شهر
                attrs={
                    'class': 'form-control',
                    'placeholder': 'آدرس شهر (اختیاری)',
                    'rows': 3,
                }
            ),
        }
