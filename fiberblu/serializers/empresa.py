from rest_framework.serializers import ModelSerializer, CharField
from django.db import models
from fiberblu.models.empresa import Empresa, CategoriaEmpresa

class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"
class EmpresaDetailSerializer(ModelSerializer):

    class Meta:
        model = Empresa
        fields = ("id", "nome","cnpj","endereco","email","telefone","inscricao_estadual","classificacao_fiscal","categoria")
        depth = 2

class EmpresaListSerializer(ModelSerializer):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=9)
    classificacao_fiscal = models.CharField(max_length=8)
    categoria = models.ForeignKey(CategoriaEmpresa, on_delete=models.PROTECT, related_name="empresas")


    class Meta:
        model = Empresa
        fields = ("id", "nome","cnpj","endereco","email","telefone","inscricao_estadual","classificacao_fiscal", "categoria")
        depth = 2