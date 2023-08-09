from django.contrib import admin

from .models import CategoriaProduto, GrupoProduto, LinhaProduto, Produto

admin.site.register(CategoriaProduto)
admin.site.register(GrupoProduto)
admin.site.register(LinhaProduto)
admin.site.register(Produto)