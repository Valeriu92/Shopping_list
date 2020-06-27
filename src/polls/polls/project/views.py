from django.shortcuts import render,redirect
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


    item = ShoppingItem.objects.filter(list = pk)
    form = ShoppingItemsForm()
    curent_user = request.user
    if request.method == 'POST':
        form = ShoppingItemsForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit = False)
            form2.list_id = pk
            form.save()
        return redirect('items',pk = pk)

    context = {
        'shopping_item': item,
        'form': form,
        'curent': curent_user
    }

    return render(request, 'listItems.html', context)


def Delete_ShoppingList(request, pk):
    list = ShoppingList.objects.get(id = pk)

    if request.method == 'POST':
        list.delete()
        return redirect ("list")

    context = {
        'list': list
    }
    return render(request, 'delete_List.html', context)

def Delete_ShoppinItem(request, pk):

    item = ShoppingItem.objects.get(id = pk)
    listid = item.list_id

    if request.method == 'POST':
        item.delete()
        return redirect('items', pk = listid)

    context = {

        'item': item
    }

    return render(request, 'delete_item.html', context)

def Update_ShoppingItem(request, pk):
    item = ShoppingItem.objects.get(id = pk)
    listid = item.list_id
    form = ShoppingItemsForm(instance=item)

    if request.method == 'POST':
        form = ShoppingItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items', pk = listid)

    context = {
        'form': form
    }
    return render(request, 'update_item.html', context)


