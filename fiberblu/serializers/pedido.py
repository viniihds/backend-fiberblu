from rest_framework.serializers import CharField, ModelSerializer

from fiberblu.models.pedido import Pedido

from .produto import ProdutoSerializer


class PedidoSerializer(ModelSerializer):
    produtos = ProdutoSerializer(many=True)
    representante = CharField(source="representante.nome")
    usuario = CharField(source="usuario.email")
    empresa = CharField(source="empresa.nome")
    status = CharField(source="get_status_display")
    pagamento = CharField(source="pagamento.descricao")

    class Meta:
        model = Pedido
        fields = "__all__"
