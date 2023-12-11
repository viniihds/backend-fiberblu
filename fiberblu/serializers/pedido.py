from rest_framework.serializers import CharField, ModelSerializer

from fiberblu.models.pedido import Pedido, ItensPedido
from fiberblu.serializers.pedido import Pedido, ItensPedido

class ItensPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = ["produto", "quantidade"]

class PedidoSerializer(ModelSerializer):
    itens = ItensPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ("id", "usuario", "status", "total", "pagamento", "empresa", "itens", "data", "dataPagamento", "valor")
        depth = 1
