from django.contrib import admin

from campagnes.models import Campagne, Enseigne, Magasin, Rayon, CampagneAdmin, MagasinAdmin, RayonAdmin, \
    PlanificationCampagne, PlanificationCampagneAdmin


admin.site.register(Campagne, CampagneAdmin)
admin.site.register(Enseigne)
admin.site.register(Magasin, MagasinAdmin)
admin.site.register(Rayon, RayonAdmin)
admin.site.register(PlanificationCampagne, PlanificationCampagneAdmin)
