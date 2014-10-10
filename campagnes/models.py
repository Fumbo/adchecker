from django.db import models


class Campagne(models.Model):
    nom = models.CharField(max_length=50)
    annonceur = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return "%s" % self.nom



class Enseigne(models.Model):
    nom = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return "%s" % self.nom


class Magasin(models.Model):
    enseigne = models.ForeignKey(Enseigne)
    ville = models.CharField(max_length=30)
    identifiant = models.PositiveSmallIntegerField(unique=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['enseigne']

    def __str__(self):
        return "%s" % self.ville


class Rayon(models.Model):
    nom = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return "%s" % self.nom
