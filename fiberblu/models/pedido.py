from django.db import models

from .empresa import Empresa
from .produto import Produto
from .representante import Representante
from .pagamento import Pagamento


class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto, related_name="pedidos")
    representante = models.ForeignKey(Representante, on_delete=models.PROTECT, related_name="pedidos")
    valor = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    data = models.DateField(max_length=10)
    dataPagamento = models.DateField(max_length=10)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name="pedidos")
    pagamento = models.ForeignKey(Pagamento, on_delete=models.PROTECT, related_name="pagamentos")

    def __str__(self):
        return f"Pedido {self.empresa}"
