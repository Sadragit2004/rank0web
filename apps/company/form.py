from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['mobile_number', 'fullname', 'is_call']
        widgets = {
            'mobile_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'شماره موبایل'}),
            'fullname': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'اسم کامل'}),
            'is_call': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
