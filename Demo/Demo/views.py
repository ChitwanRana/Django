from django.http import HttpResponse,HttpRequest
from django.shortcuts import render

def home(request):
     # return HttpResponse("Hello , Welcome to Home page")
     return render(request,'index.html')

def contact(request):
     return HttpResponse("Welcome to Contact Page")

def about(request):
     return HttpResponse("Welcome to about page ")