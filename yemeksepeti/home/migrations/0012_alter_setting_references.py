# Generated by Django 4.1.3 on 2022-12-26 23:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_setting_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000),
        ),
    ]
