# Generated by Django 3.0.14 on 2022-06-24 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ayush', '0004_rooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_signup',
            old_name='status',
            new_name='status_user',
        ),
    ]
