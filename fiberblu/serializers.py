from rest_framework.serializers import ModelSerializer

from fiberblu.models import CategoriaProduto, LinhaProduto, GrupoProduto, Produto

class CategoriaProdutoSerializer(ModelSerializer):
    class Meta:
        model = CategoriaProduto
        fields = "__all__"

class LinhaProdutoSerializer(ModelSerializer):
    class Meta:
        model = LinhaProduto
        fields = "__all__"

class GrupoProdutoSerializer(ModelSerializer):
    class Meta:
        model = GrupoProduto
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

