from django import forms


class SearchForm(forms.Form):

    price1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'','placeholder':''}))
    price2 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'','placeholder':''}))
