from django.conf.urls import url
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="index"),
    path('contact/', views.contact, name="contact"),
    path('article/P<id>-P<slug>', views.read, name="read"),
    path('accueil/P<id_article>', views.view_article),
    path('accueil/P<year>/P<month>', views.list_articles),
    path('date', views.date_actuelle),
    path('addition/P<nombre1>/P<nombre2>/', views.addition)
]
