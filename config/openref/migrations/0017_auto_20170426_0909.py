# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openref', '0016_auto_20170426_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerupdate',
            name='provider',
            field=models.ForeignKey(default=1, error_messages={'blank': 'INVALID!!11', 'null': 'NULL11!'}, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='openref.Provider'),
        ),
    ]