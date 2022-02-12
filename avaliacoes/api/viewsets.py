from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .seriealizers import AvaliacaoSerializer


class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer