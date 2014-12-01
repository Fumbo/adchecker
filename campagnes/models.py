from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


# ################################################################################
# Enseigne
class Enseigne(models.Model):
    nom = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return "%s" % self.nom


# ################################################################################
# Magasin
class Magasin(models.Model):
    identifiant = models.CharField(max_length=50)
    ville = models.CharField(max_length=30)
    enseigne = models.ForeignKey(Enseigne)

    class Meta:
        ordering = ['enseigne']

    def __str__(self):
        return "%s" % self.ville


class MagasinAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'identifiant', 'enseigne')
    list_filter = ('enseigne',)


# ###############################################################################
# Rayon
class Rayon(models.Model):
    nom = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True)
    magasin = models.ForeignKey(Magasin)

    def __str__(self):
        return "%s>%s>%s" % (self.magasin.enseigne.nom, self.magasin.ville, self._get_ancestors())

    def _get_ancestors(self):
        if self.parent:
            return "%s>%s" % (self.parent._get_ancestors(), self.nom)
        else:
            return self.nom


class RayonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'parent')


# ###############################################################################
# Campagne
class Campagne(models.Model):
    nom = models.CharField(max_length=50)
    annonceur = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return "%s" % self.nom


class CampagneAdminForm(forms.ModelForm):
    def clean(self):
        if self.cleaned_data['date_debut'] > self.cleaned_data['date_fin']:
            raise forms.ValidationError('La date de fin ne doit pas preceder '
                                        'la date de debut')
        return self.cleaned_data

    class Meta:
        model = Campagne
        exclude = []


class CampagneAdmin(admin.ModelAdmin):
    form = CampagneAdminForm
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple}
    }


# ###############################################################################
# Planification Campagne
class PlanificationCampagne(models.Model):
    campagne = models.ForeignKey(Campagne)
    date_execution = models.DateTimeField()
    rayon = models.ForeignKey(Rayon)
    status = models.CharField(max_length=4)  # PASS|FAIL|BUG|SKIP