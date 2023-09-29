from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuarios(AbstractUser):
    bolsas_choices = [
        ('Coordenador do Projeto', 'Coordenador do Projeto'),
        ('Coordenador do Eixo','Coordenador do Eixo'),
        ('Bolsista Superior','Bolsista Superior'),
        ('Bolsista Medio','Bolsista Medio'),
    ]

    cpf = models.CharField(max_length=11)
    carga_horaria = models.PositiveIntegerField(default=0)
    tipo_bolsa = models.CharField(max_length=100, choices=bolsas_choices)

    