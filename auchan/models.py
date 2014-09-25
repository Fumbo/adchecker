from django.db import models

# Create your models here.


class Drive(models.Model):
    ville = models.CharField(max_length=30)
    identifiant = models.PositiveSmallIntegerField(unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "%s-%s" % (self.ville, self.identifiant)
