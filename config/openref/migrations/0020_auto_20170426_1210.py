# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 19:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openref', '0019_auto_20170426_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='providerupdate',
            old_name='providerupdate_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='providerupdate_created_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='providerupdate_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='providerupdate_modified',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='providerupdate_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='providerupdate_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='providerupdate',
            old_name='providerupdate_providerid',
            new_name='providerid',
        ),
    ]