# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openref', '0018_auto_20170426_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='providerupdate',
            old_name='created',
            new_name='providerupdate_created',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='created_by',
            new_name='providerupdate_created_by',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='description',
            new_name='providerupdate_description',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='modified',
            new_name='providerupdate_modified',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='name',
            new_name='providerupdate_name',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='price',
            new_name='providerupdate_price',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='provider',
            new_name='providerupdate_providerid',
        ),
    ]
