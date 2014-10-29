# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class ExecutionBatch(models.Model):
    environment = models.CharField(max_length=2000, blank=True)
    host = models.CharField(max_length=150, blank=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    arguments = models.CharField(max_length=2000, blank=True)
    default_case_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'execution_batch'


class TestCase(models.Model):
    label = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'test_case'


class TestCaseExecution(models.Model):
    description = models.CharField(max_length=300, blank=True)
    result = models.CharField(max_length=7, blank=True)
    execution_batch_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'test_case_execution'


class TestCaseExecutionAddressPart(models.Model):
    part = models.CharField(max_length=200, blank=True)
    case_execution_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'test_case_execution_address_part'


class TestCycle(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    running_count = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'test_cycle'


class TestCycleTestCaseExecution(models.Model):
    test_cycle_id = models.IntegerField(primary_key=True)
    case_execution_id = models.IntegerField()
    include_in_reporting = models.NullBooleanField()

    class Meta:
        db_table = 'test_cycle_test_case_execution'
