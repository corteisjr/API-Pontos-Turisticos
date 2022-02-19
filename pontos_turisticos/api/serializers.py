from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.seriealizers import EnderecosSerializer
from comentarios.api.seriealizers import ComentarioSerializer
from avaliacoes.api.seriealizers import AvaliacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecosSerializer()
    comentarios = ComentarioSerializer(many=True)
    
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos')
        
    def get_descricao_completa(self, obj):
        return "%s"