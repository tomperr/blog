from django.db import models
from fonctions import *
import os

# Create your models here

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

class SpeedPost(models.Model):

    contenu = models.TextField(max_length=200)
    parution = models.DateTimeField(auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to=path_and_rename, blank=True, null=True)

    def __str__(self):
        return self.contenu

class Lien(models.Model):

    nom_lien = models.TextField(max_length=None)
    lienHttp = models.TextField(max_length=None)

    def __str__(self):
        return self.nom_lien
