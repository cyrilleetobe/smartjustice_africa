from django.db import models
import uuid


class Signalement(models.Model):
    TYPE_CHOICES = [
        ('corruption', 'Corruption judiciaire'),
        ('violation', 'Violation de droits'),
        ('fuite', 'Fuite de donnees'),
    ]
    STATUT_CHOICES = [
        ('recu', 'Recu'),
        ('en_cours', 'En cours de traitement'),
        ('traite', 'Traite'),
        ('classe', 'Classe sans suite'),
    ]
    code_anonyme = models.CharField(max_length=20, unique=True, editable=False)
    type_signalement = models.CharField(max_length=20, choices=TYPE_CHOICES)
    tribunal_concerne = models.CharField(max_length=200)
    date_incident = models.DateField()
    description_chiffree = models.TextField()
    preuves_chiffrees = models.TextField(blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='recu')
    date_soumission = models.DateTimeField(auto_now_add=True)
    checksum = models.CharField(max_length=64, editable=False)

    def save(self, *args, **kwargs):
        if not self.code_anonyme:
            self.code_anonyme = 'SJ-' + str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code_anonyme} - {self.type_signalement}"