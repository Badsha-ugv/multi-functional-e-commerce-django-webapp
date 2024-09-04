from django import forms 
from .models import Order 


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ['first_name','last_name','email','address','city','post_code']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'post_code':forms.TextInput(attrs={'class':'form-control'})
            
        }