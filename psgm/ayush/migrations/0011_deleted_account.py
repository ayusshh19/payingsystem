# Generated by Django 3.0.14 on 2022-06-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayush', '0010_login_log_last_logout'),
    ]

    operations = [
        migrations.CreateModel(
            name='deleted_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'del',
                'verbose_name_plural': 'dels',
                'db_table': 'delacc',
                'managed': True,
            },
        ),
    ]
