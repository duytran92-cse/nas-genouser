# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-27 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20170324_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResetPassToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userresetpasstoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.User'),
        ),
    ]
