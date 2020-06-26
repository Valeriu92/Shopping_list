from django import forms
from django.forms import ModelForm

from .models import *

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = '__all__'

class ShoppingItemsForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = '__all__'
