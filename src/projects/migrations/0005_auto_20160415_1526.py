# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 15:26
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20160415_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectProgress',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
        migrations.AddField(
            model_name='task',
            name='actualDate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='expectedDate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskState',
            field=models.CharField(choices=[('AW', 'Awaiting'), ('IP', 'In Progress'), ('CP', 'Completed')], default='AW', max_length=200),
        ),
    ]
