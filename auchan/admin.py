from django.contrib import admin
from auchan.models import Drive

# Register your models here.


class DriveAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')

admin.site.register(Drive, DriveAdmin)
