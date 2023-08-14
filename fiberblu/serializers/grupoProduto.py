from rest_framework.serializers import ModelSerializer
from fiberblu.models.grupoProduto import GrupoProduto

class GrupoProdutoSerializer(ModelSerializer):
    class Meta:
        model = GrupoProduto
        fields = "__all__"