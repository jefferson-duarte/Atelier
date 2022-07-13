from django.db import models


class CreatePost(models.Model):
    titulo = models.CharField(max_length=255)
    descricao_curta = models.CharField(max_length=255)
    descricao_longa = models.TextField()
    
    def __str__(self):
        return self.titulo
