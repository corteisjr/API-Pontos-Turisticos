from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from endereco.models import Enderecos


class EnderecosSerializer(ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ('id','linha1', 'linha2', 'provincia', 'cidade')