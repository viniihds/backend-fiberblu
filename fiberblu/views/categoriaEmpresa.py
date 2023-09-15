from rest_framework.viewsets import ModelViewSet

from fiberblu.models.categoriaEmpresa import CategoriaEmpresa
from fiberblu.serializers.categoriaEmpresa import CategoriaEmpresaSerializer


class CategoriaEmpresaViewSet(ModelViewSet):
    queryset = CategoriaEmpresa.objects.all()
    serializer_class = CategoriaEmpresaSerializer
