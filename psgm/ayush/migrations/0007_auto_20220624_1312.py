# Generated by Django 3.0.14 on 2022-06-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayush', '0006_auto_20220624_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_log',
            name='last_logout',
        ),
        migrations.AddField(
            model_name='login_log',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='login_log',
            name='min_login',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
