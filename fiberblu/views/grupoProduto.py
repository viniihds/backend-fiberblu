from rest_framework.viewsets import ModelViewSet

from fiberblu.models.grupoProduto import GrupoProduto
from fiberblu.serializers.grupoProduto import GrupoProdutoSerializer


class GrupoProdutoViewSet(ModelViewSet):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer
