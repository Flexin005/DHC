# Generated by Django 3.0.6 on 2020-06-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_delete_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image1_url',
            field=models.CharField(blank=True, max_length=1000000),
        ),
        migrations.AddField(
            model_name='category',
            name='image2_url',
            field=models.CharField(blank=True, max_length=1000000),
        ),
    ]
