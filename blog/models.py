from django.db import models

# Create your models here.

class Categorie(models.Model):

    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Article(models.Model):

    titre = models.CharField(max_length=100)
    contenu = models.TextField(max_length=None)

    parution = models.DateField(auto_now=False, auto_now_add=True)
    last_modif = models.DateField(auto_now=True, auto_now_add=False)

    categorie = models.ForeignKey('Categorie')
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.titre