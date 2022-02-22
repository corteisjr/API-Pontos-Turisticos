from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao
from pontos_turisticos.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.seriealizers import EnderecosSerializer
from comentarios.api.seriealizers import ComentarioSerializer
from avaliacoes.api.seriealizers import AvaliacaoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecosSerializer(read_only=True)
    comentarios = ComentarioSerializer(many=True)
    descricao_completa = SerializerMethodField()
    
    
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos', 'descricao_completa')
        read_only_fields = ('comentarios', 'avaliacoes')
    
    def create_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
          
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.create_atracoes(atracoes, ponto)
        return ponto
        
        
    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.nome, obj.descricao)