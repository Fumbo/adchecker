from django.contrib import admin

from campagnes.models import Campagne, Enseigne, Magasin, Rayon, CampagneAdmin, MagasinAdmin, RayonAdmin, \
    PlanificationCampagne, PlanificationCampagneAdmin, EnseigneAdmin


admin.site.register(Campagne, CampagneAdmin)
admin.site.register(Enseigne, EnseigneAdmin)
admin.site.register(Magasin, MagasinAdmin)
admin.site.register(Rayon, RayonAdmin)
admin.site.register(PlanificationCampagne, PlanificationCampagneAdmin)
