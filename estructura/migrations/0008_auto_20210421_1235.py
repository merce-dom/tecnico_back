# Generated by Django 3.1.7 on 2021-04-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0007_auto_20210406_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='equipos'),
        ),
    ]
