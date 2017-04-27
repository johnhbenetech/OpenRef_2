# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openref', '0015_auto_20170426_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerupdate',
            name='provider',
            field=models.ForeignKey(default=1, error_messages={'invalid': 'you custom error message'}, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='openref.Provider'),
        ),
    ]