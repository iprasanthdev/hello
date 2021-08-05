from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms

tasks = ["new"]

class NewForm(forms.Form):
    task = forms.CharField(label="Add your task")
# Create your views here.
def index(request):
    return render(request,"task/index.html",
    {"taskdic":tasks}
    )

def add(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tas:index"))
        else:
            return render(request,"task/add.html",{
               "form":form
             })
    return render(request,"task/add.html",{
        "form":NewForm()
    })