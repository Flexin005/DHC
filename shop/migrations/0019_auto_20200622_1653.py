# Generated by Django 3.0.6 on 2020-06-22 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20200613_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestoffer',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='bestoffer',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='bestoffer',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='bestoffer',
            name='url1',
        ),
        migrations.RemoveField(
            model_name='bestoffer',
            name='url2',
        ),
        migrations.RemoveField(
            model_name='bestoffer',
            name='url3',
        ),
    ]
