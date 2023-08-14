from rest_framework.serializers import ModelSerializer
from fiberblu.models.pedido import Pedido

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"