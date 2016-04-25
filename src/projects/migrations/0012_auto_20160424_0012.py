# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-23 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20160423_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='difficultyLevel',
            field=models.IntegerField(choices=[(1, 'Easy'), (3, 'Medium'), (5, 'Difficult')], default=1, max_length=200),
        ),
    ]