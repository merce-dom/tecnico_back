# Generated by Django 3.1.7 on 2021-06-24 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0003_auto_20210621_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repuesto',
            name='stock',
        ),
    ]
