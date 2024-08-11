from django import forms
from .models import Item

INPUT_CLASS = 'w-full py-4 px-3 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('categories', 'name', 'description', 'price', 'image')

        widgets = {
            'categories': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Name'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Description'
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Price'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            })

        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'name', 'description', 'price', 'image', 'is_sold')

        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Name'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Description'
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Price'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            })

        }
        
