# Generated by Django 3.0.14 on 2022-06-24 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ayush', '0007_auto_20220624_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_log',
            name='min_login',
        ),
    ]
