from django.contrib import admin

from .models import ( CategoriaEmpresa, CategoriaProduto, Empresa, GrupoProduto, LinhaProduto, Pedido, ItensPedido, Produto, Representante, Pagamento )

admin.site.register(CategoriaProduto)
admin.site.register(GrupoProduto)
admin.site.register(LinhaProduto)
admin.site.register(Produto)
admin.site.register(CategoriaEmpresa)
admin.site.register(Empresa)
admin.site.register(Representante)
admin.site.register(ItensPedido)
admin.site.register(Pagamento)

class ItensPedidoInline(admin.TabularInline):
    model = ItensPedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItensPedidoInline]