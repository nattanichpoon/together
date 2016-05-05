# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-05 15:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20160425_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
