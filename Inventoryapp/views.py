from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')
    
@login_required(login_url='user-login')  
def staff(request):
    workers = User.objects.all()
    context = {
        'workers' : workers
    }
    return render(request, 'dashboard/staff.html', context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers' : workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all() #Using ORM
    # items = Product.objects.raw('SELECT * FROM dashboard_product') 
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
        
    else:
        form = ProductForm()
    
    context = {
        'items': items,
        'form' : form,
    }
    return render(request, 'dashboard/products.html', context)

@login_required(login_url='user-login')
def product_delete(request, pk): #pk - primary key
    item = Product.objects.get(id=pk)
    
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-products') 
    
    return render(request, 'dashboard/product_delete.html')

@login_required(login_url='user-login')
def product_update(request, pk):
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
        
    context={
        'form' : form,
    }
    return render(request, 'dashboard/product_update.html', context)



@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    
    context = {
        'orders' : orders,
    }
    return render(request, 'dashboard/order.html', context)
    
