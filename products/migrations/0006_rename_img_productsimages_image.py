# Generated by Django 4.2 on 2024-09-07 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_img_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsimages',
            old_name='img',
            new_name='image',
        ),
    ]
