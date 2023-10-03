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

# @admin.register(Autor)
# class AutorAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'email')
#     search_fields = ('nome', 'email')
#     list_filter = ('nome',)
#     ordering = ('nome', 'email')

# @admin.register(Categoria)
# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = ('descricao',)
#     search_fields = ('descricao',)
#     list_filter = ('descricao',)
#     ordering = ('descricao',)

# @admin.register(Editora)
# class EditoraAdmin(admin.ModelAdmin):
#     list_display = ('nome',)
#     search_fields = ('nome',)
#     list_filter = ('nome',)
#     ordering = ('nome',)

# @admin.register(Livro)
# class LivroAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'editora', 'categoria')
#     search_fields = ('titulo', 'editora__nome', 'categoria__descricao')
#     list_filter = ('editora', 'categoria')
#     ordering = ('titulo', 'editora', 'categoria')
#     list_per_page = 25