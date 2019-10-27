from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from . models import Product

from . forms import ProductForm

# def price(request):
#     return HttpResponse('This item is 1000Rs.')


def list_products(request):
    products=Product.objects.all()

    return render(request, 'products.html',{'products':products})

def create_product(request):
    form=ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_products)

    return render(request,'product-form.html',{'form':form})


def update_product(request,id):
    product=Product.objects.get(id=id)
    
    form=ProductForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
        return redirect(list_products)
    
    return render(request,'product-form.html',{'form':form,'product':product})
    
def delete_product(request,id):
    product=Product.objects.get(id=id)
    
    if request.method=='POST':
        product.delete()
        return redirect(list_products)
    
    return render(request,'product-delete.html',{'product':product})