from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import *
from .forms import *


@login_required(login_url='login')
def Display_ShoppingList(request):
    current_user = request.user
    lista = ShoppingList.objects.filter(owner=current_user)

    form = ShoppingListForm()
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            form2.owner.add(current_user)
        return redirect("list")

    context = {
        'shopping_list': lista,
        'form': form
    }

    return render(request, 'shoppingListTemplate.html', context)


@login_required(login_url='login')
def Update_ShoppingList(request, pk):
    # item = ShoppingList.objects.get(id = pk)
    item = get_object_or_404(ShoppingList, id=pk)
    current_user = request.user
    lista = ShoppingList.objects.filter(owner=current_user)
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
            return redirect("list")

    context = {
        'form': form
    }

    if flag == 1:
        return render(request, 'update_list.html', context)
    else:
        return redirect("list")


@login_required(login_url='login')
def Delete_ShoppingList(request, pk):
    # list = ShoppingList.objects.get(id = pk)
    list = get_object_or_404(ShoppingList, id=pk)
    current_user = request.user
    listeOwner = ShoppingList.objects.filter(owner=current_user)
    flag = 0;
    for items in listeOwner:
        if pk == items.id:
            flag = 1;
        else:
            pass

    if request.method == 'POST':
        list.delete()
        return redirect("list")

    context = {
        'list': list
    }

    if flag == 1:
        return render(request, 'delete_List.html', context)
    else:
        return redirect("list")


@login_required(login_url='login')
def Display_ShoppingItem(request, pk):
    item = ShoppingItem.objects.filter(list=pk)
    list = ShoppingList.objects.get(id = pk)
    form = ShoppingItemsForm()
    current_user = request.user
    listeOwner = ShoppingList.objects.filter(owner=current_user)
    flag = 0;

    for items in listeOwner:
        if pk == items.id:
            flag = 1;
        else:
            pass

    if request.method == 'POST':
        form = ShoppingItemsForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.list_id = pk
            form2.save()
        return redirect('items', pk=pk)

    context = {
        'shopping_item': item,
        'listname':list,
        'form': form,
    }

    # return render(request, 'listItems.html', context)

    if flag == 1:
        return render(request, 'listItems.html', context)
    else:
        return redirect("list")


@login_required(login_url='login')
def Delete_ShoppinItem(request, pk):
    # item = ShoppingItem.objects.get(id = pk)
    item = get_object_or_404(ShoppingItem, id=pk)
    listid = item.list_id
    current_user = request.user
    listeOwner = ShoppingList.objects.filter(owner=current_user)
    flag = 0;

    for items in listeOwner:
        if listid == items.id:
            flag = 1;
        else:
            pass

    if request.method == 'POST':
        item.delete()
        return redirect('items', pk=listid)

    context = {

        'item': item
    }

    if flag == 1:
        return render(request, 'delete_item.html', context)
    else:
        return redirect("list")


@login_required(login_url='login')
def Update_ShoppingItem(request, pk):
    # item = ShoppingItem.objects.get(id = pk)
    item = get_object_or_404(ShoppingItem, id=pk)
    listid = item.list_id
    form = ShoppingItemsForm(instance=item)
    current_user = request.user
    listeOwner = ShoppingList.objects.filter(owner=current_user)
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
            return redirect('items', pk=listid)

    context = {
        'form': form,
        'item': item
    }

    if flag == 1:
        return render(request, 'update_item.html', context)
    else:
        return redirect("list")
