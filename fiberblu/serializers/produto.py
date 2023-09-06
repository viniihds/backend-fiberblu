from rest_framework.serializers import ModelSerializer, CharField
from fiberblu.models.produto import Produto

class ProdutoSerializer(ModelSerializer):
    linha = CharField(source='linha.descricao')
    grupo = CharField(source='grupo.descricao')
    categoria = CharField(source='categoria.descricao')
    class Meta:
        model = Produto
        fields = "__all__"
