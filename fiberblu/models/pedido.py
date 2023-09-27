from django.db import models

from usuario.models import Usuario

from .empresa import Empresa
from .produto import Produto
from .pagamento import Pagamento

class Pedido(models.Model):
    class StatusPedido(models.IntegerChoices):
        CARRINHO = (1,"Carrinho",)
        REALIZADO = (2,"Realizado",)
        PAGO = (3,"Pago",)
        ENTREGUE = (4,"Entregue",)

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusPedido.choices,  default=StatusPedido.CARRINHO)
    valor = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    data = models.DateField(max_length=10)
    dataPagamento = models.DateField(max_length=10)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name="pedidos")
    pagamento = models.ForeignKey(Pagamento, on_delete=models.PROTECT, related_name="pagamentos")

    def __str__(self):
        return f"Pedido {self.empresa}"

class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)