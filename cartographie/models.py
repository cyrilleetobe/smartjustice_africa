from django.db import models


class Tribunal(models.Model):
    nom = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    dossiers_total = models.IntegerField(default=0)
    dossiers_en_attente = models.IntegerField(default=0)
    dossiers_traites = models.IntegerField(default=0)
    magistrats = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} - {self.ville}"

    def taux_traitement(self):
        if self.dossiers_total == 0:
            return 0
        return round((self.dossiers_traites / self.dossiers_total) * 100, 1)