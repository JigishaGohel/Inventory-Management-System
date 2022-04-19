from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')
    
    
def staff(request):
    return render(request, 'dashboard/staff.html')

def product(request):
    return render(request, 'dashboard/products.html')

def order(request):
    return render(request, 'dashboard/order.html')
    
