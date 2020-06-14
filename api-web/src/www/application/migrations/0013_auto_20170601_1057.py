# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-06-01 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_userupload_uservariation_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservariation',
            name='science_filter',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='science_filter',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userupload',
            name='text',
            field=models.TextField(default='', max_length=4294967295),
        ),
    ]