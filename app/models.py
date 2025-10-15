from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nome
