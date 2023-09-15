from rest_framework.serializers import ModelSerializer

from fiberblu.models.empresa import Empresa


class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"
