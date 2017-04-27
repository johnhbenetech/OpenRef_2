# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 15:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openref', '0013_auto_20170426_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]