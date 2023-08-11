from rest_framework.viewsets import ModelViewSet

from fiberblu.models import CategoriaProduto, LinhaProduto, GrupoProduto, Produto, Representante, Empresa, CategoriaEmpresa
from fiberblu.serializers import CategoriaProdutoSerializer, LinhaProdutoSerializer, GrupoProdutoSerializer, ProdutoSerializer, RepresentanteSerializer, EmpresaSerializer, CategoriaEmpresaSerializer

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

class RepresentanteViewSet(ModelViewSet):
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer

class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class CategoriaEmpresaViewSet(ModelViewSet):
    queryset = CategoriaEmpresa.objects.all()
    serializer_class = CategoriaEmpresaSerializer