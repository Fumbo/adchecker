# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('environment', models.CharField(max_length=2000, blank=True)),
                ('host', models.CharField(max_length=150, blank=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('arguments', models.CharField(max_length=2000, blank=True)),
                ('default_case_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'execution_batch',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'db_table': 'test_case',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCaseExecution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300, blank=True)),
                ('result', models.CharField(max_length=7, blank=True)),
                ('execution_batch_id', models.IntegerField(null=True, blank=True)),
                ('case_id', models.IntegerField(null=True, blank=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'test_case_execution',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCaseExecutionAddressPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part', models.CharField(max_length=200, blank=True)),
                ('case_execution_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'test_case_execution_address_part',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('description', models.CharField(max_length=300, blank=True)),
                ('running_count', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'test_cycle',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCycleTestCaseExecution',
            fields=[
                ('test_cycle_id', models.IntegerField(primary_key=True)),
                ('case_execution_id', models.IntegerField(serialize=False, primary_key=True)),
                ('include_in_reporting', models.NullBooleanField()),
            ],
            options={
                'db_table': 'test_cycle_test_case_execution',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, blank=True)),
                ('password_crypt', models.CharField(max_length=80, blank=True)),
            ],
            options={
                'db_table': 'user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('field_create_time', models.DateTimeField(null=True, db_column='_create_time', blank=True)),
                ('create_micros', models.IntegerField(null=True, blank=True)),
                ('value', models.CharField(max_length=44, blank=True)),
                ('remaining_uses', models.IntegerField(null=True, blank=True)),
                ('expires', models.DateTimeField(null=True, blank=True)),
                ('revoked', models.NullBooleanField()),
            ],
            options={
                'db_table': 'user_token',
            },
            bases=(models.Model,),
        ),
    ]
