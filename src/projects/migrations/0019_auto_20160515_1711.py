# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20160509_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='expectedDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
