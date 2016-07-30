# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import unixtimestampfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('language', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=255)),
                ('uid', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created', unixtimestampfield.fields.UnixTimeStampField()),
                ('changed', unixtimestampfield.fields.UnixTimeStampField()),
                ('comment', models.IntegerField()),
                ('promote', models.BooleanField()),
                ('moderate', models.BooleanField()),
                ('sticky', models.BooleanField()),
                ('tnid', models.IntegerField()),
                ('translate', models.BooleanField()),
            ],
            options={
                'db_table': 'node',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NodeRevisions',
            fields=[
                ('vid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('teaser', models.TextField()),
                ('log', models.TextField()),
                ('timestamp', unixtimestampfield.fields.UnixTimeStampField()),
                ('format', models.IntegerField()),
            ],
            options={
                'db_table': 'node_revisions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('val', models.CharField(max_length=200)),
                ('str_ini', unixtimestampfield.fields.UnixTimeStampField(default=b'0.0')),
                ('float_ini', unixtimestampfield.fields.UnixTimeStampField(default=0.0)),
                ('int_ini', unixtimestampfield.fields.UnixTimeStampField(default=0)),
                ('dt_ini', unixtimestampfield.fields.UnixTimeStampField(default=django.utils.timezone.now)),
                ('num_field', unixtimestampfield.fields.UnixTimeStampField(default=0.0)),
                ('int2_field', unixtimestampfield.fields.UnixTimeStampField(default=0)),
                ('int3_field', unixtimestampfield.fields.UnixTimeStampField(default=0)),
                ('int4_field', unixtimestampfield.fields.UnixTimeStampField(default=0)),
            ],
        ),
    ]