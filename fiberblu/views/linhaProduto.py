from rest_framework.viewsets import ModelViewSet

from fiberblu.models.linhaProduto import LinhaProduto
from fiberblu.serializers.linhaProduto import LinhaProdutoSerializer


class LinhaProdutoViewSet(ModelViewSet):
    queryset = LinhaProduto.objects.all()
    serializer_class = LinhaProdutoSerializer
