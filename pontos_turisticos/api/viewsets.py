from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    
    def get_queryset(self):
        # Filtragem de queryset
        return   PontoTuristico.objects.filter(aprovado=True)
    
    # Sobscrevendo  a action de GET

    def list(self, request, *args, **kwargs):
        return Response({'Teste': 123})
    
    #Sobscrevendo a action POST
    def create(self, request, *args, **kwargs):
        return Response({'hello'  : request.data['nome']})