from django import forms
from django.forms import ModelForm

from .models import *

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ('name',)

class ShoppingItemsForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ('name','quantity','gramaj','marca','magazin','complete',)
