from rest_framework.viewsets import ModelViewSet
from fiberblu.models.representante import Representante
from fiberblu.serializers.representante import RepresentanteSerializer

class RepresentanteViewSet(ModelViewSet):
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer