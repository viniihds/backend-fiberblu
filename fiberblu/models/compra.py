from django.db import models

from usuario.models import Usuario

from .produto import Produto


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        REALIZADO = (
            1,
            "Realizado",
        )
        ENTREGUE = (
            2,
            "Entregue",
        )

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.REALIZADO)


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)
