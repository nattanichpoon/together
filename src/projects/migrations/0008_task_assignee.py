# -*- coding: utf-8 -*-

# Generated by Django 1.9.1 on 2016-04-20 07:46
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc

# Generated by Django 1.9.1 on 2016-04-16 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0007_auto_20160415_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
