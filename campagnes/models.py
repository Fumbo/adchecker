from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from mptt.models import MPTTModel, TreeForeignKey


# ################################################################################
# Enseigne
class Enseigne(models.Model):
    nom = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return "%s" % self.nom


class EnseigneAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')


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
class Rayon(MPTTModel):
    nom = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __str__(self):
        if self.parent:
            return "%s>%s" % (self.parent.__str__(), self.nom)
        else:
            return self.nom

    def get_path(self):
        if self.parent:
            return "%s/%s" % (self.parent.get_path(), self.path)
        else:
            return self.identifiant


class RayonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'parent')


# ###############################################################################
# Campagne
def content_file_name(instance, filename):
    return '/'.join(['upload', instance.id + '_' + instance.nom, filename])


class Campagne(models.Model):
    nom = models.CharField(max_length=50)
    annonceur = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    publicite = models.ImageField(upload_to=content_file_name)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return "%s" % self.nom


class CampagneAdminForm(forms.ModelForm):
    def clean(self):
        if all(x in self.cleaned_data for x in ['date_debut', 'date_fin']) \
                and self.cleaned_data['date_debut'] > self.cleaned_data['date_fin']:
            raise forms.ValidationError('La date de fin ne doit pas preceder '
                                        'la date de debut')
        return self.cleaned_data

    class Meta:
        model = Campagne
        exclude = []


class CampagneAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')
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
    magasin = models.ForeignKey(Magasin)
    status = models.CharField(max_length=4)  # PASS|FAIL|BUG|SKIP|WAIT
    screenshot = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.screenshot


class PlanificationCampagneAdmin(admin.ModelAdmin):
    list_display = ('campagne', 'magasin', 'rayon', 'date_execution', 'screenshot', 'status')
