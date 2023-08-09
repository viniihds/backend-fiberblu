from rest_framework.viewsets import ModelViewSet

from fiberblu.models import CategoriaProduto, LinhaProduto
from fiberblu.serializers import CategoriaProdutoSerializer, LinhaProduto

class CategoriaProdutoViewSet(ModelViewSet):
    queryset = CategoriaProduto.objects.all()
    serializer_class = CategoriaProdutoSerializer

class LinhaProdutoViewSet(ModelViewSet):
    queryset = LinhaProduto.objects.all()
    serializer_class = LinhaProdutoSerializer