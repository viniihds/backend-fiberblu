from rest_framework.viewsets import ModelViewSet

from fiberblu.models.produto import Produto
from fiberblu.serializers.produto import ProdutoSerializer,ProdutoListSerializer, ProdutoDetailSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer
