from django.contrib import admin
from campagnes.models import Enseigne, Drive
# Register your models here.


class DriveAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    list_filter = ('enseigne',)

admin.site.register(Drive, DriveAdmin)
admin.site.register(Enseigne)
