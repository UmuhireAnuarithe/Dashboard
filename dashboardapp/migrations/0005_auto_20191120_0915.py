# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-20 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0004_auto_20191114_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='snippet',
            field=models.ImageField(upload_to=b'question/'),
        ),
    ]
