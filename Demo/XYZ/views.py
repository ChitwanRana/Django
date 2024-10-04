from django.shortcuts import render
from django.http import HttpResponse
from .models import Chaivarity
from django.shortcuts import get_object_or_404

# Create your views here.
def abc(request):
     chais=Chaivarity.objects.all()
     return render(request,'XYZ/abc.html',{'chais':chais})

def abcd(request):
     return HttpResponse("Hello welcome to abcd")


def chai_detail(request,chai_id):
     chai=get_object_or_404(Chaivarity,pk=chai_id)
     return render(request,'XYZ/detail.html',{'chai':chai})


def chai_store_view(request):
     return render(request,'XYZ/store.html')