from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from .forms import HotelForm
from .models import Hotel


def yuri(request):
    return HttpResponse('Yuri is lerning.')

def hotel_image_view(request):
    
    if request.method == 'POST':
        form = HotelForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=HotelForm()
    return render(request,'image.html',{'form':form})

def success(request):
    return HttpResponse('successfully upload')

def display_hotel_images(request):
    if request.method=='GET':
        Hotels=Hotel.objects.all()
        
    return render(request,'view_image.html',{'hotel_images':Hotels})

