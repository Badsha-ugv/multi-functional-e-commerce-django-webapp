from django import forms 

class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)