# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160922_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='wdth_field',
            new_name='width_field',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', upload_to=posts.models.upload_location, width_field='width_field'),
        ),
    ]
