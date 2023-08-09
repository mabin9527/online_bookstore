from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    widgets = {
            'image': forms.ClearableFileInput(attrs={'label': 'Image'}),
        }

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories_list = Category.objects.all()
        friendly_names = [
            (c.cid, c.get_friendly_name()) for c in categories_list
            ]
        self.fields['category'].label = 'Category'
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-secondary rounded'
            