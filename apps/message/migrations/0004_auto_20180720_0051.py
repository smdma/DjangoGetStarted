# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-19 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20180719_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户留言信息', 'verbose_name_plural': '用户留言信息'},
        ),
    ]
