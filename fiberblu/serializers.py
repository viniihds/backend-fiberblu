from rest_framework.serializers import ModelSerializer

from fiberblu.models import CategoriaProduto, LinhaProduto

class CategoriaProdutoSerializer(ModelSerializer):
    class Meta:
        model = CategoriaProduto
        fields = "__all__"

class LinhaProdutoSerializer(ModelSerializer)
    class Meta:
        model = LinhaProduto
        fields = "__all__"

