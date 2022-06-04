from django.db import models
from distutils.command.upload import upload


class Contato(models.Model):
    nome = models.CharField(max_length=20)
    sobre_nome = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50, verbose_name='Endereço')
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')

    def __str__(self):
        return self.nome
        