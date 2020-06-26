from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=250)
    user_age = models.IntegerField()


    def __str__(self):
        return self.user_name + ' ' + str(self.user_age)


class ShoppingList(models.Model):
    name = models.CharField(max_length= 50, null = False)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_lists')
    date_created = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    name = models.CharField(max_length= 50, null = False)
    quantity = models.IntegerField(default=0)
    gramaj = models.CharField(max_length= 20, null = True)
    marca = models.CharField(max_length= 50, null = False)
    magazin = models.CharField(max_length= 50, null = False)
    list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='shopping_item')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + str(self.quantity) + ' ' + self.gramaj + ' ' + self.marca + ' ' + self.magazin
