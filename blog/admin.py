from django.contrib import admin
from .models import *

# Class admin

class ArticleAdmin(admin.ModelAdmin):

    model = Article
    list_display = ['titre', 'parution', 'categorie']
    list_filter = ['titre', 'last_modif']
    search_fields = ['titre', 'categorie']

    class Media:
        js = ('/static/admin/js/article_admin.js',)

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(SpeedPost)
admin.site.register(Lien)