from django.shortcuts import render, get_object_or_404
from blog.models import Article, Categorie, SpeedPost, Lien

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
    # articles = Article.objects.all()
    article = get_object_or_404(Article, id=id, slug=slug)

    to_return = {'article': article, 'categories': cats}

    if str(article.categorie) == "Jeux vidéos":
        mes_plus = str(article.les_plus).split("\n")
        to_return["plus"] = mes_plus

        mes_moins = str(article.les_moins).split("\n")
        to_return["moins"] = mes_moins

        to_return["is_plus_moins"] = True

    else:
        to_return["is_plus_moins"] = False

    return render(request, 'blog/lire.html', to_return)

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

def liens(request):
    liens = Lien.objects.all()
    mes_liens = list(liens)
    mes_liens.reverse()
    return render(request, 'blog/liens.html', {'mes_liens': mes_liens})
