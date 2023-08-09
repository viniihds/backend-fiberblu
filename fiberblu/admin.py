from django.contrib import admin

from .models import CategoriaProduto, GrupoProduto, LinhaProduto, Produto, CategoriaEmpresa, Empresa

admin.site.register(CategoriaProduto)
admin.site.register(GrupoProduto)
admin.site.register(LinhaProduto)
admin.site.register(Produto)
admin.site.register(CategoriaEmpresa)
admin.site.register(Empresa)