from rest_framework.serializers import ModelSerializer
from fiberblu.models.categoriaProduto import CategoriaProduto

class CategoriaProdutoSerializer(ModelSerializer):
    class Meta:
        model = CategoriaProduto
        fields = "__all__"
