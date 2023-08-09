from rest_framework.viewsets import ModelViewSet

from fiberblu.models import CategoriaProduto, LinhaProduto, GrupoProduto, Produto
from fiberblu.serializers import CategoriaProdutoSerializer, LinhaProdutoSerializer, GrupoProdutoSerializer, ProdutoSerializer

class CategoriaProdutoViewSet(ModelViewSet):
    queryset = CategoriaProduto.objects.all()
    serializer_class = CategoriaProdutoSerializer

class LinhaProdutoViewSet(ModelViewSet):
    queryset = LinhaProduto.objects.all()
    serializer_class = LinhaProdutoSerializer

class GrupoProdutoViewSet(ModelViewSet):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer