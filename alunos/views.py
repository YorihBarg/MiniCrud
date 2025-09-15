from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cadastro (request):
    return render(request, 'cadastro.html')

def index (request):
    return render(request, 'index.html')

def cadastrados (request):
    return render(request, 'cadastrados.html')

def salva_aluno (request):
    nome_aluno = request.POST['nome_aluno']
    sobrenome_aluno = request.POST['sobrenome_aluno']
    nascimento_aluno = request.POST['nascimento_aluno']
    curso_aluno = request.POST['curso_aluno']
    return render(request, 'casdastro.html', context={'nome_aluno': nome_aluno})

