# Generated by Django 4.2.2 on 2023-08-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_querydatabase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querydatabase',
            name='qphone',
            field=models.IntegerField(),
        ),
    ]
