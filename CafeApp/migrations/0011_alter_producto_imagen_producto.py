# Generated by Django 4.1.2 on 2022-11-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafeApp', '0010_remove_producto_imagen_producto_imagen_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_producto',
            field=models.ImageField(blank=True, null=True, upload_to='items/'),
        ),
    ]