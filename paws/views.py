from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def food(request):
    return render(request,'food.html')

def shelter(request):
    return render(request,'shelter.html')

def info(request):
    return render(request,'info.html')