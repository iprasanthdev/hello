from django.shortcuts import render

task = ['food','cloths','living room work']
# Create your views here.
def index(request):
    return render(request,"task/index.html",
    {"tasks":task}
    )

def add(request):
    return render(request,"task/add.html")