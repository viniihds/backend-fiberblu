from rest_framework.viewsets import ModelViewSet
from fiberblu.models.categoriaProduto import CategoriaProduto
from fiberblu.serializers.categoriaProduto import CategoriaProdutoSerializer

class CategoriaProdutoViewSet(ModelViewSet):
    queryset = CategoriaProduto.objects.all()
    serializer_class = CategoriaProdutoSerializer