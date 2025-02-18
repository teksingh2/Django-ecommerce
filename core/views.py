from django.shortcuts import render,redirect
from core.forms import *
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'core/index.html',{'products':products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # include request.FILES for handling image uploads
        if form.is_valid():
            form.save()
            messages.info(request,'Product Added Successfully')
            return redirect('/')  # Redirect to product list page or any other page
    else:
        form = ProductForm()
    categories = Category.objects.all()  # Fetch all categories
    

    return render(request, "core/add_product.html", {"form": form, "categories": categories})

