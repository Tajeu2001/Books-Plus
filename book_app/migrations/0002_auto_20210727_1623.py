# Generated by Django 2.2.24 on 2021-07-27 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='contact',
        ),
    ]
