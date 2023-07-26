from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sai(request):
    return HttpResponse('heeeee....')
def new2(request):
    return render(request,'new2.html')
def ind2(request):
    return render(request,'ind2.html')  