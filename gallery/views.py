from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Author,Picture,Category,Location

# Create your views here.

def pics(request):
    category = Category.get_categories()
    pictures = Picture.all_pics()
    location_pics = Location.get_location()

    return render(request,'pics.html',{'pictures': pictures, 'category': category, 'location_pics':location_pics })
