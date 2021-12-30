from django import forms
from django.contrib.auth import models
from django.forms import fields
from django.forms.models import ModelForm
from .models import Product,Order
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Permission






from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['product','order_quantity']

class StaffForm(forms.ModelForm):
    class Meta:
        model=User
        
        fields=['username','email','first_name']
