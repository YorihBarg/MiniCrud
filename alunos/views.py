from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno

# Create your views here.
def index (request):
    return render(request, 'index.html')

def cadastro_alunos(request):
    if request.method == 'POST':
        nome_aluno = request.POST['nome_aluno']
        sobrenome = request.POST['sobrenome_aluno']
        curso = request.POST['curso_aluno']
        email = request.POST['email_aluno']
        data_nascimento = request.POST['data_nascimento_aluno']

        Aluno.objects.create(
            nome=nome_aluno,
            sobrenome=sobrenome,
            curso=curso,
            email=email,
            data_nascimento=data_nascimento
        )
        return redirect('cadastrados')

    return render(request, 'cadastro.html')

def listar_alunos(request):
   alunos = Aluno.objects.all()
   return render(request, 'cadastrados.html', {'alunos': alunos})
