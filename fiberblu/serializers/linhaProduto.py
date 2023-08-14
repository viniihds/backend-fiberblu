from rest_framework.serializers import ModelSerializer
from fiberblu.models.linhaProduto import LinhaProduto

class LinhaProdutoSerializer(ModelSerializer):
    class Meta:
        model = LinhaProduto
        fields = "__all__"