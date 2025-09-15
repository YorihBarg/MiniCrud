from django.urls import path 
from . import views

#UrlConf
urlpatterns = [
    path('', views.index),
    path('salva_aluno', views.salva_aluno),
]