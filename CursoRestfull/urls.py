from atexit import register
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewset import AtracoesViewSet
from endereco.api.viewsets import EnderecosViewSet

router = routers.DefaultRouter()
router.register(r'pontoturisticos', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet)
router.register(r'enderecos', EnderecosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
