# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-03 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_auto_20170602_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank='true', default='static/diary/images/bri.jpg', upload_to='profile_image'),
        ),
    ]
