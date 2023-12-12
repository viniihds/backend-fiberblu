from rest_framework.viewsets import ModelViewSet

from fiberblu.models.empresa import Empresa
from fiberblu.serializers.empresa import EmpresaSerializer, EmpresaDetailSerializer, EmpresaListSerializer


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return EmpresaListSerializer
        elif self.action == "retrieve":
            return EmpresaDetailSerializer
        return EmpresaSerializer
