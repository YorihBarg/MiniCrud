from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    curso = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
