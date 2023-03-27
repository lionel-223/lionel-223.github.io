from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('services.html', views.services, name='services'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('contact.html', views.contact, name='contact'),
    path('cv.html', views.cv, name='cv'),
    path('blogs.html', views.blogs, name='blogs'),
    path('resultat.html', views.resultat, name='resultat'),
]