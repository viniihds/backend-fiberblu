from rest_framework.serializers import ModelSerializer, CharField

from fiberblu.models import Compra, ItensCompra



class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 1

class CompraSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True)
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    class Meta:
        model = Compra
        fields = "__all__"

