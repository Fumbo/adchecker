from django.contrib import admin
from campagnes.models import Enseigne, Magasin
# Register your models here.


class MagasinAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    list_filter = ('enseigne',)

admin.site.register(Magasin, MagasinAdmin)
admin.site.register(Enseigne)
