from rest_framework.serializers import ModelSerializer, CharField

from fiberblu.models.empresa import Empresa

class EmpresaSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    class Meta:
        model = Empresa
        fields = "__all__"
