# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 02:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.TimeField(default=datetime.datetime(2016, 9, 29, 2, 27, 17, 596453, tzinfo=utc)),
            preserve_default=False,
        ),
    ]