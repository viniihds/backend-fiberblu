from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from fiberblu.views import (
    CategoriaEmpresaViewSet,
    CategoriaProdutoViewSet,
    CompraViewSet,
    EmpresaViewSet,
    GrupoProdutoViewSet,
    LinhaProdutoViewSet,
    PedidoViewSet,
    ProdutoViewSet,
    RepresentanteViewSet,
    PagamentoViewSet,
)
from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"categoriaproduto", CategoriaProdutoViewSet)
router.register(r"linhaproduto", LinhaProdutoViewSet)
router.register(r"grupoproduto", GrupoProdutoViewSet)
router.register(r"produto", ProdutoViewSet)
router.register(r"representante", RepresentanteViewSet)
router.register(r"empresa", EmpresaViewSet)
router.register(r"categoriaempresa", CategoriaEmpresaViewSet)
router.register(r"pedido", PedidoViewSet)
router.register(r"compra", CompraViewSet)
router.register(r"pagamento", PagamentoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
]
