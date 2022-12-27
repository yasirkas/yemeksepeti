from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import forms
from .models import Setting, ContactForm, ContactFormMessage

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarı ile gönderilmiştir!")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting,'form':'form'}
    return render(request, 'contact.html', context)

def referans(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'referans'}
    return render(request, 'referans.html', context)
