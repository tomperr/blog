from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Article, Categorie, SpeedPost

# Create your views here.

cats = Categorie.objects.all()
articles = Article.objects.all()

def accueil(request):
    cats = Categorie.objects.all()
    articles = Article.objects.all()
    mes_arts = list(articles)
    mes_arts.reverse()
    if len(mes_arts) >= 1:
        last = mes_arts[len(mes_arts)-1]
    else:
        last = False
    return render(request, 'blog/accueil.html', {'derniers_articles': mes_arts, 'last': last, 'categories': list(cats)})

def lire(request, id, slug):
    cats = Categorie.objects.all()
    articles = Article.objects.all()
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article': article, 'categories': cats})

def categories(request, cat):
    cats = Categorie.objects.all()
    articles = Article.objects.all()
    mes_arts = list()
    for art in articles:
        if str(art.categorie.nom).lower() == cat:
            mes_arts.append(art)
    mes_arts.reverse()
    if len(mes_arts) >= 1:
        last = mes_arts[len(mes_arts)-1]
    else:
        last = False
    return render(request, 'blog/accueil.html', {'derniers_articles': mes_arts, 'last': last, 'categories': list(cats)})

def speedpost(request):
    posts = SpeedPost.objects.all()
    mes_posts = list(posts)
    mes_posts.reverse()
    return render(request, 'blog/speedpost.html', {'posts': mes_posts})