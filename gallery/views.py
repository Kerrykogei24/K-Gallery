from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Author

# Create your views here.

def pic(request):
    
    return render(request,'pics.html')
