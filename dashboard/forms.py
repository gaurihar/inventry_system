from django import forms
from django.contrib.auth import models
from django.forms import fields
from django.forms.models import ModelForm
from .models import Product,Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['product','order_quantity']
