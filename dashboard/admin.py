from django.contrib import admin
from .models import CATEGORY, Product,Order
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header="Inventory System Dashboard"

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','quantity','category')
    list_filter=('category',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)

# admin.site.unregister(Group)
