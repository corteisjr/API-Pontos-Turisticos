from django.contrib.auth.models import User
from django.db import models


class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField()
    data = models.DataTimeField(auto_now_add=True)


    def __str__(self):
        return user.first_name


