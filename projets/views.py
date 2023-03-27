from django.shortcuts import render
from flask import Flask
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import parametres
from projets.models import Mes_Articles

from django.http import HttpResponse



def about(request):
    return render(request,'about.html',)
def services(request):
    return render(request,'services.html',)

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    article = Mes_Articles.objects.filter(Id_Mes_Articles=1)
    context = {'article': article}
    return render(request, 'portfolio.html', context)

def contact(request):
    return render(request, 'contact.html')
def cv(request):
    return render(request, 'cv.html')
def blogs(request):
    return render(request, 'blogs.html')
def resultat(request):
    print('/thanks/')
    return render(request, 'resultat.html')
