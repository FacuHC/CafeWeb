# Generated by Django 4.1.2 on 2022-11-26 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafeApp', '0015_alter_order_items_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='precio_total',
        ),
        migrations.AlterField(
            model_name='order',
            name='items_cliente',
            field=models.CharField(max_length=100),
        ),
    ]
