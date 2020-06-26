from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import *
from .forms import *


def hello(request):
    return HttpResponse("Hello Valeriu")

def Display_Users(request):
    abc = Users.objects.all()
    context = {
        'nume': abc,
        'orice': 'ana are mere'

    }

    return render(request,'display_users.html',context)

def Display_ShoppingList(request):
    lista = ShoppingList.objects.all
    form = ShoppingListForm()

    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("mumu")


    context = {
        'shopping_list': lista,
        'aiurea': 'aiurea',
        'form': form
    }

    return render(request, 'shoppingListTemplate.html', context)



def Display_ShoppingItem(request, pk):
    #lists = ShoppingList.objects.filter(id = pk)

    #for list in lists:
    item = ShoppingItem.objects.filter(list = pk)
    form = ShoppingItemsForm()
    context = {
        'shopping_item': item,
        'form': form
    }

    return render(request, 'listItems.html', context)