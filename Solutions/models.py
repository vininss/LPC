from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=128, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=128, blank=True, null=True)
    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField('Status', max_length=128, blank=True, null=True)
    def __str__(self):
        return self.nome

class Chamado(models.Model):
    titulo = models.CharField('Titulo', max_length=128, blank=True, null=True)
    autor = models.ForeignKey(Funcionario, on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.TextField('Descrição', max_length=500, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    data_abertura = models.DateTimeField(auto_now_add=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return 'CH{}BR - {} - {}'.format(self.id, self.titulo, self.status)

class Atendimento(models.Model):
    descricao = models.TextField('Descrição', max_length=500, blank=True, null=True)
    autor = models.ForeignKey(Funcionario, on_delete=models.CASCADE, blank=True, null=True)
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
            return '{} - {} - {}'.format(self.chamado, self.descricao, self.autor)
