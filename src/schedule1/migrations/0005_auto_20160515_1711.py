# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule1', '0004_auto_20160513_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meetingTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingAgenda',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingSummary',
            field=models.CharField(max_length=1000),
        ),
    ]
