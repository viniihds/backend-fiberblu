from rest_framework.viewsets import ModelViewSet
from fiberblu.models.empresa import Empresa
from fiberblu.serializers.empresa import EmpresaSerializer

class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer