from django.contrib import admin

from .models import Setting,ContactFormMessage,ContactForm

# Register your models here.

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','status']
    list_filter = ['status']

admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(Setting)