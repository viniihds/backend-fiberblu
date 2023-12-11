from rest_framework.serializers import CharField, ModelSerializer

from fiberblu.models.produto import Produto


class ProdutoSerializer(ModelSerializer):


    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1
