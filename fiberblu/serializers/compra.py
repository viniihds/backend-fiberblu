from rest_framework.serializers import ModelSerializer

from fiberblu.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"