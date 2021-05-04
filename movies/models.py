from django.db import models
from uuid import uuid4

# Create your models here.

class Movies(models.Model):
    idMovie = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Titulo = models.CharField(max_length=255)
    ano = models.IntegerField()
    diretor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    avaliacao = models.IntegerField(null=True, default=0)
    createAt = models.DateField(auto_now_add=True)
