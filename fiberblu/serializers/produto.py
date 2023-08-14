from rest_framework.serializers import ModelSerializer
from fiberblu.models.produto import Produto

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
