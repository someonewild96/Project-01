from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "App/index.html")

def greet(request,name):
    return render(request, "App/greet.html", {
        "name": name.capitalize()
    })

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
