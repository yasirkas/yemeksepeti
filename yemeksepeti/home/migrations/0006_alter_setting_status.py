# Generated by Django 4.1.3 on 2022-12-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_setting_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
