from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponse, Http404
from blog.forms import ContactForm
from blog.models import Article


# Create your views here.
def home(request):
    """Exemple de page HTML, non valable pour que l'exemple soit concis"""
    articles = Article.objects.all()

    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def list_articles(request, month, year):
    """Liste des articles d'un mois précis. """
    text = "Vous avez demandé les articles de {0} {1}".format(month, year)
    return HttpResponse(text)


def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier paramètre est TOUJOURS la requète de
    l'utilisateur
    """
    if int(id_article) > 100:
        # si l'id est supérieur à 100, nous considérons que l'article n'éxiste pas
        raise Http404
    return HttpResponse('<h1>Mon article ici</h1>')


def read(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/read.html', {'article': article})


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    return render(request, 'blog/addition.html', locals())


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            author = form.cleaned_data['author']
            renvoi = form.cleaned_data['renvoi']
            envoi = True
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', locals())
