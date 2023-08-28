from django.db import models

from usuario.models import Usuario

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        REALIZADO = (1,"Realizado",)
        ENTREGUE = (2,"Entregue",)

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.REALIZADO)