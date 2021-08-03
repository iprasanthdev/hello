from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
#    return HttpResponse("hello world")
    return render(request,"main\main.html")
    
def greet(request,name):
    return render(request,"main/greet.html",{
        "name":name.capitalize()
    })
