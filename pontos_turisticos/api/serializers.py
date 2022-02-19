from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.seriealizers import EnderecosSerializer
from comentarios.api.seriealizers import ComentarioSerializer
from avaliacoes.api.seriealizers import AvaliacaoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecosSerializer()
    comentarios = ComentarioSerializer(many=True)
    descricao_completa = SerializerMethodField()
    
    
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos', 'descricao_completa')
        
    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.nome, obj.descricao)