from django import forms
from django.forms import ModelForm
#from django.contrib.auth.

from .models import *

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ('name',)

        labels = {
            "name": ""

        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Insert list name here",
                'data-on-text': 'Inactive'
            })

        }

class ShoppingItemsForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ('name','marca','quantity','gramaj','magazin','complete',)

        labels = {
            "name": "Name",
            "marca": "Brand",
            "gramaj": "Weight",
            "magazin": "Store",

        }


class ShoppingListFormOwner(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ('name','owner',)