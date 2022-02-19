from django.db import models

class Enderecos(models.Model):
    linha1 = models.CharField(max_length=150) #rua numero
    linha2 = models.CharField(max_length=150) #bairro
    provincia = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    latitude = models.IntegerField(blank=True, null=True)
    longititude = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return self.linha1
