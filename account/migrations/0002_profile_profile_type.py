# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('Childminder', 'Childminder'), ('Parent', 'Parent')], default='Childminder', max_length=11),
        ),
    ]