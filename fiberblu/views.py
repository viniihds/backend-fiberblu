from rest_framework.viewsets import ModelViewSet

from fiberblu.models import CategoriaProduto
from fiberblu.serializers import CategoriaProdutoSerializer

class CategoriaProdutoViewSet(ModelViewSet):
    queryset = CategoriaProduto.objects.all()
    serializer_class = CategoriaProdutoSerializer