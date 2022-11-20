from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text="Django Kurulumu: python -m pip install -e django <br> Proje Oluşturma: django-admin startproject mysite <br>" \
         " App Ekleme: python manage.my startapp polls"
    context = {'text': text}
    return render(request, 'index.html', context)
