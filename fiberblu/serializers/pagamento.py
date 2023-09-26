from rest_framework.serializers import ModelSerializer

from fiberblu.models.pagamento import Pagamento


class PagamentoSerializer(ModelSerializer):
    class Meta:
        model = Pagamento
        fields = "__all__"
