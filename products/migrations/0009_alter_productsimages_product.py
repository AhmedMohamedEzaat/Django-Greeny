# Generated by Django 4.2 on 2024-09-08 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productsimages_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_image', to='products.product'),
        ),
    ]
