# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 19:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('assessment_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hazard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('hazard_name', models.CharField(max_length=50)),
                ('possible_risk', models.CharField(max_length=10)),
                ('possible_consequences', models.CharField(max_length=500)),
                ('preControl', models.CharField(max_length=200)),
                ('postControls', models.CharField(max_length=200)),
                ('date_to_be_completed', models.DateField()),
                ('risks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hazards', to='risks.Assessment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
