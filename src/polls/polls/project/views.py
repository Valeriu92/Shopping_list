from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
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
    current_user = request.user
    lista = ShoppingList.objects.filter(owner = current_user)

    form = ShoppingListForm()
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit = False)
            form2.save()
            form2.owner.add(current_user)
        return HttpResponseRedirect("mumu")


    context = {
        'shopping_list': lista,
        'form': form
    }

    return render(request, 'shoppingListTemplate.html', context)

def Update_ShoppingList(request, pk):
    #item = ShoppingList.objects.get(id = pk)
    item = get_object_or_404(ShoppingList, id = pk)
    current_user = request.user
    lista = ShoppingList.objects.filter(owner = current_user)
    flag = 0;
    for items in lista:
        if pk == items.id:
            flag = 1;
        else:
            pass

    form = ShoppingListFormOwner(instance=item)

    if request.method == 'POST':
        form = ShoppingListFormOwner(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect ("list")

    context = {
        'form': form
    }

    if flag==1:
        return render(request, 'update_list.html', context)
    else:
        return redirect ("list")


def Delete_ShoppingList(request, pk):
    #list = ShoppingList.objects.get(id = pk)
    list = get_object_or_404(ShoppingList, id = pk)
    current_user = request.user
    listeOwner = ShoppingList.objects.filter(owner = current_user)
    flag = 0;
    for items in listeOwner:
        if pk == items.id:
            flag = 1;
        else:
            pass

    if request.method == 'POST':
        list.delete()
        return redirect ("list")

    context = {
        'list': list
    }

    if flag==1:
        return render(request, 'delete_List.html', context)
    else:
        return redirect ("list")

@login_required(login_url='/')
def Display_ShoppingItem(request, pk):

    item = ShoppingItem.objects.filter(list = pk)
    form = ShoppingItemsForm()
    current_user = request.user
    listeOwner = ShoppingList.objects.filter(owner = current_user)
    flag = 0;

    for items in listeOwner:
        if pk == items.id:
            flag = 1;
        else:
            pass

    if request.method == 'POST':
        form = ShoppingItemsForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit = False)
            form2.list_id = pk
            form2.save()
        return redirect('items',pk = pk)

    context = {
        'shopping_item': item,
        'form': form,
        'curent': current_user
    }

    #return render(request, 'listItems.html', context)


    if flag == 1:
        return render(request, 'listItems.html', context)
    else:
        return redirect("list")


def Delete_ShoppinItem(request, pk):

    #item = ShoppingItem.objects.get(id = pk)
    item = get_object_or_404(ShoppingItem,id = pk)
    listid = item.list_id
    current_user = request.user
    listeOwner = ShoppingList.objects.filter(owner = current_user)
    flag = 0;

    for items in listeOwner:
        if listid == items.id:
            flag = 1;
        else:
            pass

    if request.method == 'POST':
        item.delete()
        return redirect('items', pk = listid)

    context = {

        'item': item
    }

    if flag == 1:
        return render(request, 'delete_item.html', context)
    else:
        return redirect("list")

def Update_ShoppingItem(request, pk):
    #item = ShoppingItem.objects.get(id = pk)
    item = get_object_or_404(ShoppingItem, id = pk)
    listid = item.list_id
    form = ShoppingItemsForm(instance=item)
    current_user = request.user
    listeOwner = ShoppingList.objects.filter(owner = current_user)
    flag = 0;

    for items in listeOwner:
        if listid == items.id:
            flag = 1;
        else:
            pass

    if request.method == 'POST':
        form = ShoppingItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items', pk = listid)

    context = {
        'form': form
    }


    if flag == 1:
        return render(request, 'update_item.html', context)
    else:
        return redirect("list")

