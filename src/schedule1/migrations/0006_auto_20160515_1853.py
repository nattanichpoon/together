# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule1', '0005_auto_20160515_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingSummary',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
