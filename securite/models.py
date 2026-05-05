from django.db import models
from django.contrib.auth.models import User


class JuridictionRole(models.Model):
    ROLE_CHOICES = [
        ('magistrat', 'Magistrat'),
        ('greffier', 'Greffier'),
        ('avocat', 'Avocat'),
        ('opj', 'Officier de Police Judiciaire'),
        ('admin', 'Administrateur'),
    ]
    TRIBUNAL_CHOICES = [
        ('TGI Yaounde', 'TGI Yaounde'),
        ('TGI Douala', 'TGI Douala'),
        ('TGI Bafoussam', 'TGI Bafoussam'),
    ]
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, related_name='juridiction_role')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    tribunal = models.CharField(max_length=50, choices=TRIBUNAL_CHOICES)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.role} - {self.tribunal}"


class AuditTrail(models.Model):
    ACTION_CHOICES = [
        ('connexion', 'Connexion'),
        ('deconnexion', 'Deconnexion'),
        ('consultation', 'Consultation dossier'),
        ('modification', 'Modification dossier'),
        ('signalement', 'Signalement soumis'),
        ('export', 'Export de donnees'),
        ('acces_refuse', 'Acces refuse'),
    ]
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=30, choices=ACTION_CHOICES)
    tribunal = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    adresse_ip = models.GenericIPAddressField(null=True, blank=True)
    horodatage = models.DateTimeField(auto_now_add=True)
    immuable = models.BooleanField(default=True, editable=False)
    checksum = models.CharField(max_length=64, editable=False)

    class Meta:
        ordering = ['-horodatage']

    def save(self, *args, **kwargs):
        import hashlib
        contenu = f"{self.utilisateur}{self.action}{self.description}{self.adresse_ip}"
        self.checksum = hashlib.sha256(contenu.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.horodatage} - {self.action} - {self.utilisateur}"


class AlerteSecurite(models.Model):
    NIVEAU_CHOICES = [
        ('info', 'Information'),
        ('warning', 'Avertissement'),
        ('critical', 'Critique'),
    ]
    niveau = models.CharField(max_length=10, choices=NIVEAU_CHOICES)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    tribunal = models.CharField(max_length=50, blank=True)
    resolue = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.niveau} - {self.titre}"