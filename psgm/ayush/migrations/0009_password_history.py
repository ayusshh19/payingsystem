# Generated by Django 3.0.14 on 2022-06-24 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ayush', '0008_remove_login_log_min_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='password_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_modified', models.DateTimeField(auto_now=True)),
                ('no_changed', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ayush.user_signup')),
            ],
            options={
                'verbose_name': 'his',
                'verbose_name_plural': 'hiss',
                'db_table': 'history',
                'managed': True,
            },
        ),
    ]