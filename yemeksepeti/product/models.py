from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Category(models.Model):
    STATUS = {
        ('True', 'Evet'),
        ('False', 'Hayır'),
    }
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=250)
    description = models.DateTimeField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src= "{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

# Product class olusturuldu.
class Product(models.Model):
    STATUS = {
        ('True', 'Evet'),
        ('False', 'Hayır'),
    }
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=250)
    description = models.DateTimeField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src= "{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src= "{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

