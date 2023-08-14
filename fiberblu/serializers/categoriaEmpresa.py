from rest_framework.serializers import ModelSerializer
from fiberblu.models.categoriaEmpresa import CategoriaEmpresa

class CategoriaEmpresaSerializer(ModelSerializer):
    class Meta:
        model = CategoriaEmpresa
        fields = "__all__"
