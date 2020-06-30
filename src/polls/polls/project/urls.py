from django.urls import path
from .views import  *

urlpatterns = [
    path('',Display_Users),
    path('mumu',Display_ShoppingList, name="list"),
    path('items/<int:pk>/', Display_ShoppingItem, name="items"),
    path('delete_list/<int:pk>/', Delete_ShoppingList, name="delete_list"),
    path('delete_item/<int:pk>/', Delete_ShoppinItem, name="delete_item"),
    path('update_item/<int:pk>/', Update_ShoppingItem, name="update_item"),
    path('update_list/<int:pk>/', Update_ShoppingList, name="update_list")

]