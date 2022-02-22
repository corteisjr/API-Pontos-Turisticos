from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated,]
    # authentication_classes = (TokenAuthentication,)
    serializer_class = PontoTuristicoSerializer
    lookup_field = 'nome'
    def get_queryset(self):
        # Filtragem de queryset
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset.filter(nome=nome)
        
        if descricao:
            queryset.filter(descricao=descricao)
                
        return   PontoTuristico.objects.filter(aprovado=True)
    
    # Action personalizada

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass
    
    @action(
        methods=['get'], 
        detail=False
    )
    def teste(self, request):
        pass
    
    # @action(methods=['post'], detail=True)
    # def associar_atracoes(self, request, pk):
    #     atracoes = request.data['ids']
    #     ponto = PontoTuristico.objects.get(id=pk)
    #     ponto.atracoes.set(atracoes)
    #     ponto.save()
    #     return ponto
        
    # Sobscrevendo  a action de GET


    # def list(self, request, *args, **kwargs):
    #     return Response({'Teste': 123})
    
    #Sobscrevendo a action POST
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
       return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
        
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
