from rest_framework.serializers import CharField, ModelSerializer
from django.db import models
from fiberblu.models.produto import Produto
from fiberblu.models.produto import CategoriaProduto
from fiberblu.models.produto import LinhaProduto
from fiberblu.models.produto import GrupoProduto



class ProdutoSerializer(ModelSerializer):


    class Meta:
        model = Produto
        fields = ("id", "cor","volume","preco","categoria","linha","grupo")

class ProdutoDetailSerializer(ModelSerializer):

    class Meta:
        model = Produto
        fields = ("id", "cor","volume","preco","categoria","linha","grupo")
        depth = 2

class ProdutoListSerializer(ModelSerializer):
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.PROTECT, related_name="produtos")
    volume = models.IntegerField(null=False)
    preco = models.DecimalField(max_digits=8, null=False, decimal_places=2)
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.PROTECT, related_name="produtos")
    linha = models.ForeignKey(LinhaProduto, on_delete=models.PROTECT, related_name="produtos")
    grupo = models.ForeignKey(GrupoProduto, on_delete=models.PROTECT, related_name="produtos")

    class Meta:
        model = Produto
        fields = ("id", "cor","volume","preco","categoria","linha","grupo")
        depth = 2