# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-30 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20170330_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.CharField(default='', max_length=255),
        ),
    ]
