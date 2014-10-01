from django.db import models

# Create your models here.


class Enseigne(models.Model):
    nom = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return "%s" % self.nom


class Drive(models.Model):
    enseigne = models.ForeignKey(Enseigne)
    ville = models.CharField(max_length=30)
    identifiant = models.PositiveSmallIntegerField(unique=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['enseigne']

    def __str__(self):
        return "%s-%s" % (self.ville, self.identifiant)
