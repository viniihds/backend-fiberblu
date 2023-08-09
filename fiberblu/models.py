from django.db import models

class CategoriaProduto (models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class LinhaProduto (models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class GrupoProduto (models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Produto (models.Model):
    cor = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    codigo = models.IntegerField(null = False)
    preco = models.DecimalField(max_digits=8, null = False, decimal_places = 2)
    categoria = models.ForeignKey(
        CategoriaProduto, on_delete=models.PROTECT, related_name="produtos"
    )
    linha = models.ForeignKey(
        LinhaProduto, on_delete=models.PROTECT, related_name="produtos"
    )
    grupo = models.ForeignKey(
        GrupoProduto, on_delete=models.PROTECT, related_name="produtos"
    )


    def __str__(self):
        return f"{self.categoria} {self.cor} {self.volume}"
