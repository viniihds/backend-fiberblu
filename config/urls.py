from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from fiberblu.views import (
    CategoriaEmpresaViewSet,
    CategoriaProdutoViewSet,
    EmpresaViewSet,
    GrupoProdutoViewSet,
    LinhaProdutoViewSet,
    PedidoViewSet,
    ProdutoViewSet,
    RepresentanteViewSet,
    PagamentoViewSet,
)
from usuario.router import router as usuario_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
 
router = DefaultRouter()
router.register(r"categoriaprodutos", CategoriaProdutoViewSet)
router.register(r"linhaprodutos", LinhaProdutoViewSet)
router.register(r"grupoprodutos", GrupoProdutoViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"representantes", RepresentanteViewSet)
router.register(r"empresas", EmpresaViewSet)
router.register(r"categoriaempresas", CategoriaEmpresaViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"pagamentos", PagamentoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
   # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
