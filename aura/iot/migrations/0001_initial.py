# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-13 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Device_id', models.CharField(max_length=100)),
                ('Device_name', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Device_status', models.BooleanField(default=False)),
                ('End_time', models.IntegerField(default=0)),
                ('Start_time', models.IntegerField(default=0)),
                ('Device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.Items')),
            ],
        ),
    ]