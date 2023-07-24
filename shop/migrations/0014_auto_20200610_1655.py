# Generated by Django 3.0.6 on 2020-06-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200610_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image1_url',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image2_url',
        ),
        migrations.AddField(
            model_name='category',
            name='image1',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
        migrations.AddField(
            model_name='category',
            name='image2',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
    ]