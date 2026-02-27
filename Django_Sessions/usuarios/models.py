from django.db import models
from django.contrib.auth.models import User

class EnderecoUsuario(models.Model):
    rua = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=8)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.usuario