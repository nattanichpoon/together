# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-08 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_task_taskprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskProgress',
            field=models.IntegerField(default=0, null=True),
        ),
    ]