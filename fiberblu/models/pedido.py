from django.db import models
from .empresa import Empresa
from .produto import Produto
from .representante import Representante


class Pedido (models.Model):
    produtos = models.ManyToManyField(Produto, related_name="pedidos")
    representante = models.ForeignKey(
        Representante, on_delete=models.PROTECT, related_name="pedidos"
    )
    valor = models.DecimalField(max_digits=10, null = False, decimal_places=2)
    data = models.CharField(max_length=10)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, related_name= "pedidos"
    )

    def __str__(self):
        return f"Pedido {self.empresa}"