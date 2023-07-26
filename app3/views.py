from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sai(rquest):
    return HttpResponse('hhiiiii....')
def ind3(request):
    return render(request,'ind3.html')
def new3(request):
    return render(request,'new3.html')