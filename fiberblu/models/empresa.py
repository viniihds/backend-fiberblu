from django.db import models

from .categoriaEmpresa import CategoriaEmpresa


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=9)
    classificacao_fiscal = models.CharField(max_length=8)
    categoria = models.ForeignKey(CategoriaEmpresa, on_delete=models.PROTECT, related_name="empresas")

    def __str__(self):
        return self.nome
