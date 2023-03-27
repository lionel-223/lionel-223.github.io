from django.shortcuts import render
from flask import Flask
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import parametres
from projets.models import MesArticles

from django.http import HttpResponse



def about(request):
    return render(request,'about.html',)
def services(request):
    return render(request,'services.html',)

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    article = MesArticles(Libelle_MA='Mon article', Description='Ceci est mon article', Date_publication='2022-03-28', Date_Miseajour='2022-03-28')
    article.save()
    articles = MesArticles.objects.all()
    return render(request, 'portfolio.html', {'articles': articles})

def contact(request):
    return render(request, 'contact.html')
def cv(request):
    return render(request, 'cv.html')
def blogs(request):
    return render(request, 'blogs.html')
def resultat(request):
    print('/thanks/')
    return render(request, 'resultat.html')
