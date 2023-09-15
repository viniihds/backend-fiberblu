from rest_framework.viewsets import ModelViewSet

from fiberblu.models.produto import Produto
from fiberblu.serializers.produto import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
