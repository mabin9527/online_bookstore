from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_mobile_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_city': 'City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County or State ',
        }
        aria_labels = {
            'default_mobile_number': 'Phone number for the user',
            'default_postcode': 'Postal code for the user',
            'default_city': 'City for the user',
            'default_street_address1': 'Street address 1 for the user',
            'default_street_address2': 'Street address 2 for the user',
            'default_county': 'County or state for the user',
        }
        self.fields['default_mobile_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['aria-label'] = aria_labels[
                    field
                ]
                self.fields[field].label = placeholders[field]
            else:
                self.fields[field].label
                