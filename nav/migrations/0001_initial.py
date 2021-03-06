# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('vid', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('weight', models.SmallIntegerField()),
                ('language', models.CharField(max_length=12)),
                ('trid', models.IntegerField()),
            ],
            options={
                'db_table': 'term_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TermNode',
            fields=[
                ('vid', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'term_node',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UrlAlias',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('src', models.CharField(max_length=128)),
                ('dst', models.CharField(max_length=128)),
                ('language', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'URL Alias',
                'db_table': 'url_alias',
                'managed': False,
                'verbose_name_plural': 'URL Aliases',
            },
        ),
        migrations.CreateModel(
            name='TermHierarchy',
            fields=[
                ('term', models.OneToOneField(db_column=b'tid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='hier', serialize=False, to='nav.Term')),
            ],
            options={
                'db_table': 'term_hierarchy',
                'managed': False,
            },
        ),
    ]
