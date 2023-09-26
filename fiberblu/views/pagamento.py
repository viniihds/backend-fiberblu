from rest_framework.viewsets import ModelViewSet

from fiberblu.models.pagamento import Pagamento
from fiberblu.serializers.pagamento import PagamentoSerializer


class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer