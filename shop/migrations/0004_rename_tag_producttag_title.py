# Generated by Django 4.0.4 on 2022-05-15 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_producttag_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttag',
            old_name='tag',
            new_name='title',
        ),
    ]
