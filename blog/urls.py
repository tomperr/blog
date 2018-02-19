from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.accueil, name="accueil"),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', views.lire, name="lire"),
    url(r'^categorie/(?P<cat>.+)$', views.categories, name="categories"),
    url(r'^speedpost/(?P<page>\d+)$', views.speedpost, name="speedpost"),
    url(r'^liens$', views.liens, name="liens"),
]