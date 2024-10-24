from django.db import models

class Epreuve(models.Model):
    discipline = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_heure = models.DateTimeField()
    lieu = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.discipline} ({self.date_heure})"
