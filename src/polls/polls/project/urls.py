from django.urls import path
from .views import  hello, Display_Users, Display_ShoppingItem, Display_ShoppingList

urlpatterns = [
    path('',Display_Users),
    path('mumu',Display_ShoppingList),
    path('items/<int:pk>/', Display_ShoppingItem, name="items")
]