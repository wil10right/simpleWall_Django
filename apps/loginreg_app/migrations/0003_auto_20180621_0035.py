# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-21 00:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg_app', '0002_auto_20180621_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='message_id',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='user_id',
            new_name='user',
        ),
    ]
