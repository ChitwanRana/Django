from django.shortcuts import render
from django.http import HttpResponse
from .models import Chaivarity

# Create your views here.
def abc(request):
     chais=Chaivarity.objects.all()
     return render(request,'XYZ/abc.html',{'chais':chais})

def abcd(request):
     return HttpResponse("Hello welcome to abcd")