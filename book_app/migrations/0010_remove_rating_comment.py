# Generated by Django 2.2.24 on 2021-07-30 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0009_auto_20210729_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='comment',
        ),
    ]
