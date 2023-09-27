from rest_framework.viewsets import ModelViewSet

from fiberblu.models import Compra
from fiberblu.serializers import CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
