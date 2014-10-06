from django import forms
from django.contrib import admin
from campagnes.models import Campagne, Enseigne, Magasin, Rayon


class CampagneAdminForm(forms.ModelForm):
    class Meta:
        model = Campagne
        exclude = []

    def clean(self):
        if self.cleaned_data['date_debut'] > self.cleaned_data['date_fin']:
            raise forms.ValidationError('La date de fin ne doit pas preceder '
                                        'la date de debut')
        return self.cleaned_data


class CampagneAdmin(admin.ModelAdmin):
    form = CampagneAdminForm


class MagasinAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    list_filter = ('enseigne',)

admin.site.register(Campagne, CampagneAdmin)
admin.site.register(Enseigne)
admin.site.register(Magasin, MagasinAdmin)
admin.site.register(Rayon)
