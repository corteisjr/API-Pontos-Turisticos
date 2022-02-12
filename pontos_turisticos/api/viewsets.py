from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    
    def get_queryset(self):
        # Filtragem de queryset
        return   PontoTuristico.objects.filter(aprovado=True)