# Generated by Django 4.2 on 2024-03-25 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0006_alter_productbrand_url_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbrand',
            name='url_title',
        ),
    ]
