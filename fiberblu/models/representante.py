from django.db import models


class Representante(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
