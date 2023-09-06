from rest_framework.serializers import ModelSerializer, CharField
from fiberblu.models.pedido import Pedido

class PedidoSerializer(ModelSerializer):
    produtos = CharField(source = 'produto.categoria produto.cor produto.volume')
    representante = CharField(source='representante.nome')
    empresa = CharField(source='empresa.nome')
    class Meta:
        model = Pedido
        fields = "__all__"