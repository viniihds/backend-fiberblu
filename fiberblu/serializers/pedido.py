from rest_framework.serializers import CharField, ModelSerializer

from fiberblu.models.pedido import Pedido, ItensPedido
from fiberblu.serializers.pedido import Pedido, ItensPedido

class ItensPedidoSerializer(ModelSerializer):
    produto = CharField(source="produto.linha")
    class Meta:
        model = ItensPedido
        fields = ["produto", "quantidade"]

class PedidoSerializer(ModelSerializer):
    itens = ItensPedidoSerializer(many=True, read_only=True)
    empresa = CharField(source="empresa.nome")
    pagamento = CharField(source="pagamento.descricao")
    status = CharField(source="get_status_display", read_only=True)
    usuario = CharField(source="usuario.email", read_only=True)
    
    class Meta:
        model = Pedido
        fields = ("id", "usuario", "status", "total", "pagamento", "empresa", "itens")
