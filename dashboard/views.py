from django import forms
from django.db.models import Count, Sum
from django.db.models.fields import PositiveIntegerField
from django.shortcuts import render,redirect
from django.http import response
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm,StaffForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404



# Create your views here.
# @login_required
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    if request.method=='POST':
        form =OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.customer=request.user
            form.save()
            return redirect('dashboard-index')
    else:
        form=OrderForm()

    context ={
        'orders':orders,
        'form' :form,
        'products':products
    }
    return render(request,'dashboard/index.html',context)

# @login_required
def staff(request):
    # return response.HttpResponse("this is staff page")
    workers= User.objects.all()
    

    print("work")

    context={
        'workers':workers
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):
    # return response.HttpResponse("this is staff page")
    items = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            
    else:
        form = ProductForm()
    
    # items=Product.objects.raw('select * from dashboard_product')
    context = {
            'items': items,
            'form' : form,
        } 
       

    return render(request,'dashboard/product.html',context)

@login_required
def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render (request,'dashboard/product_delete.html')

@login_required
def staff_delete(request,pk):
    del_user=User.objects.get(id=pk)
    if request.method == 'POST':
        del_user.delete()
        return redirect('dashboard-staff')
    return render (request,'dashboard/staff_delete.html')

@login_required
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('dashboard-product')
        else:
            print("not valid")    
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)


@login_required
def staff_edit(request, pk):
    item = User.objects.get(id=pk)
    user = get_object_or_404(User, pk=pk)
    print(user)
    content_type = ContentType.objects.get_for_model(User)
    print(content_type)
    permission = Permission.objects.filter(pk=pk)
    print(permission)
    

    if request.method == 'POST':
        form = StaffForm(request.POST, instance=item)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('dashboard-staff')
        else:
            print("not valid")    
    else:
        form = StaffForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/staff_edit.html', context)


@login_required
def order(request):
    # return response.HttpResponse("this is order page")
    orders=Order.objects.all()

    context={
        'orders':orders
    }
    return render(request,'dashboard/order.html',context)


