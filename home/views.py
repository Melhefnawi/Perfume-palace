from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def company(request):
    return render(request, 'home/company.html')


def help(request):
    return render(request, 'home/help.html')
