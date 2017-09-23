from django.contrib import admin
from .models import Article, Categorie

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Article)