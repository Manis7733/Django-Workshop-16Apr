from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def profile(request):
    return HttpResponse("This is profile page")

def new_home(request):
    return HttpResponse("This is  the new home page homie")