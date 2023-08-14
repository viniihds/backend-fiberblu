from rest_framework.viewsets import ModelViewSet
from fiberblu.models.pedido import Pedido
from fiberblu.serializers.pedido import PedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer