# Generated by Django 3.0.6 on 2020-06-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]