# Generated by Django 4.2.3 on 2023-07-18 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRMApp', '0004_alter_product_entered_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='Product_name',
        ),
    ]
