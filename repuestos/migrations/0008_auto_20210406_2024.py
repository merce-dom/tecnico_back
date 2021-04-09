# Generated by Django 3.1.7 on 2021-04-06 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repuestos', '0007_auto_20210406_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='preveedor',
            new_name='proveedor',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]