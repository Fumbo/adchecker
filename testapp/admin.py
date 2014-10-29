from django.contrib import admin
from testapp.models import TestCycle, TestCycleTestCaseExecution


class TestCycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'running_count')


class TestCycleTestCaseExecutionAdmin(admin.ModelAdmin):
    list_display = ('test_cycle_id', 'case_execution_id', 'include_in_reporting')

admin.site.register(TestCycle, TestCycleAdmin)
admin.site.register(TestCycleTestCaseExecution, TestCycleTestCaseExecutionAdmin)