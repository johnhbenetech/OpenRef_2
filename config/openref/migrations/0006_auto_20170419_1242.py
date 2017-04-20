# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 19:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openref', '0005_providerupdate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='providerupdate',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 19, 41, 47, 213268, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='providerupdate',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 19, 42, 0, 238571, tzinfo=utc)),
            preserve_default=False,
        ),
    ]