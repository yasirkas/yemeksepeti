# Generated by Django 4.1.3 on 2022-12-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='setting',
            name='facebook',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpemail',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtppassword',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpport',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpserver',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
