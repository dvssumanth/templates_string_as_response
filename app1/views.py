from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dvs(request):
    return HttpResponse('you need to get job')
def new(request):
    return render(request,'new.html')
def ind(request):
    return render(request,'ind.html')