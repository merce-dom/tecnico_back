# Generated by Django 3.1.7 on 2021-06-28 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0013_auto_20210628_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockminimo',
            name='almacen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks_minimos', to='repuestos.almacen'),
        ),
    ]
