from django import forms
from django.forms import ModelForm

from .models import *

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ('id','name',)

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Insert list name",
                'data-on-text': 'Inactive'
            })

        }

class ShoppingItemsForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ('name','quantity','gramaj','marca','magazin','complete',)


class ShoppingListFormOwner(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ('name','owner',)