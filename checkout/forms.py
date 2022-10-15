from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'email', 
                  'country', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',)

    def __init__(self, *args, **kwargs):
        """ Auto-generated placeholders and labels"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'email': 'Email Address',
            'country': 'Country',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Post Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False