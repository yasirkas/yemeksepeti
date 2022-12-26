from django.shortcuts import render
from django.http import HttpResponse

from .models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def faq(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'faq'}
    return render(request, 'faq.html', context)

def contact(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'contact'}
    return render(request, 'contact.html', context)

def referans(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'referans'}
    return render(request, 'referans.html', context)