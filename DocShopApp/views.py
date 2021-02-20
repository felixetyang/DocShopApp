from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'DocShopApp/index.html')


def docs(request):
    return HttpResponse('These are the list of the new documents available')