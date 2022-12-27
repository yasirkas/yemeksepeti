from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from django.forms import ModelForm, TextInput, Textarea

# Create your models here.

class Setting(models.Model):
    STATUS = {
        ('True', 'Evet'),
        ('False', 'Hayır'),
    }

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=150)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=20)
    smtpemail = models.CharField(blank=True,max_length=20)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True,max_length=100)
    instagram = models.CharField(blank=True,max_length=100)
    twitter = models.CharField(blank=True,max_length=100)
    aboutus = RichTextUploadingField(blank=True,max_length=2000)
    contact = RichTextUploadingField(blank=True,max_length=2000)
    faq = RichTextUploadingField(blank=True, max_length=2000)
    references = RichTextUploadingField(blank=True,max_length=1000)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
    )
    name = models.CharField(blank=True,max_length=50)
    email = models.CharField(blank=True,max_length=50)
    message = models.CharField(blank=True,max_length=300)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name','email','message']
        widgets = {
            'name': TextInput(attrs={'class':'input','placeholder':'Ad & Soyad'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Adresi'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Mesajınız'}),
        }
