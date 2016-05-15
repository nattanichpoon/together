# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-13 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule1', '0003_auto_20160511_1210'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='confirmedCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingAgenda',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingStatus',
            field=models.CharField(choices=[('CF', 'Confirm'), ('RJ', 'Reject'), ('PD', 'Pending')], default='PD', max_length=200),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingSummary',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]