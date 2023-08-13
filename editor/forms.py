from django import forms

from .models import StaffInfo


class StaffInfoForm(forms.ModelForm):
    class Meta:
        model = StaffInfo
        fields = [
            'name', 'age', 'create_time', 'depart', 'gender', 'mobile_number',
            'street_address1', 'address2', 'city', 'county',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'age': 'Age',
            'create_time': 'Hire Date',
            'depart': 'Department',
            'gender': 'Gender',
            'mobile_number': 'Phone Number',   
            'street_address1': 'Street Address 1',
            'address2': 'Street Address 2',
            'city': 'City',
            'county': 'County or State ',
        }
        aria_labels = {
            'name': 'Name for the staff',
            'age': 'Age for the staff',
            'create_time': 'Hire Date for the staff',
            'depart': 'Department for the staff',
            'gender': 'Gender for the staff',
            'mobile_number': 'Phone number for the staff',
            'postcode': 'Postal code for the staff',
            'street_address1': 'Street address 1 for the staff',
            'address2': 'Street address 2 for the staff',
            'city': 'City for the for the staff',
            'county': 'County or state for the staff',
        }
        self.fields['mobile_number'].widget.attrs['autofocus'] = True
        self.fields['create_time'].widget = forms.DateInput(attrs={'type': 'date'})
        for field in self.fields:
            self.fields[field].label
