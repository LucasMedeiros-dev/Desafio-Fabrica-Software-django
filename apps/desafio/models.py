from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Treinador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Pokemon(models.Model):
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    ataque_1 = models.CharField(max_length=100)
    ataque_2 = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
