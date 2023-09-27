from django.contrib import admin

from .models import ( CategoriaEmpresa, CategoriaProduto, Empresa, GrupoProduto, LinhaProduto, Pedido, Produto, Representante, Pagamento )

admin.site.register(CategoriaProduto)
admin.site.register(GrupoProduto)
admin.site.register(LinhaProduto)
admin.site.register(Produto)
admin.site.register(CategoriaEmpresa)
admin.site.register(Empresa)
admin.site.register(Representante)
admin.site.register(Pedido)
admin.site.register(Pagamento)
