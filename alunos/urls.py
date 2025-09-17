from django.urls import path 
from . import views

#UrlConf
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro_alunos, name='cadastro'),
    path('cadastrados/', views.listar_alunos, name='cadastrados'),
]