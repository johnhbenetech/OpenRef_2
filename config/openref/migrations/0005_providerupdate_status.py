# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openref', '0004_auto_20170418_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='providerupdate',
            name='status',
            field=models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('UNPROCESSED', 'Unprocessed')], default='UNPROCESSED', max_length=30),
        ),
    ]
