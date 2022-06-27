# Generated by Django 3.0.14 on 2022-06-23 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ayush', '0003_auto_20220623_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_rent', models.CharField(max_length=10)),
                ('room_description', models.CharField(max_length=500)),
                ('room_address', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ayush.user_signup')),
            ],
            options={
                'verbose_name': 'room',
                'verbose_name_plural': 'rooms',
                'db_table': 'room',
                'managed': True,
            },
        ),
    ]
