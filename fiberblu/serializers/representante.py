from rest_framework.serializers import ModelSerializer

from fiberblu.models.representante import Representante


class RepresentanteSerializer(ModelSerializer):
    class Meta:
        model = Representante
        fields = "__all__"
