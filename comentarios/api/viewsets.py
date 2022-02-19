from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .seriealizers import ComentarioSerializer
from rest_framework import filters

class ComentariosViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['comentario']