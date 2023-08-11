from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from fiberblu.views import CategoriaProdutoViewSet, LinhaProdutoViewSet, GrupoProdutoViewSet, ProdutoViewSet, RepresentanteViewSet, EmpresaViewSet, CategoriaEmpresaViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r"categoriaproduto", CategoriaProdutoViewSet)
router.register(r"linhaproduto", LinhaProdutoViewSet)
router.register(r"grupoproduto", GrupoProdutoViewSet)
router.register(r"produto", ProdutoViewSet)
router.register(r"representante", RepresentanteViewSet)
router.register(r"empresa", EmpresaViewSet)
router.register(r"categoriaempresa", CategoriaEmpresaViewSet)
router.register(r"pedido", PedidoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]