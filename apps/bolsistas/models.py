from django.db import models
from apps.eixos.models import Eixos

# Create your models here.
class Bolsista(models.Model):
    cidades_choices = [
        ('Ariquemes', 'Ariquemes'),
        ('Porto Velho', 'Porto Velho'),
        ('Alto Alegre', 'Alto Alegre'),
        ('Buritis', 'Buritis'),
        ('Cerejeiras', 'Cerejeiras'),
        ('Pimenta Bueno', 'Pimenta Bueno'),
    ]

    carga_horaria_choices = [
        ('20', '20 horas semanais'),
        ('30', '30 horas semanais'),
        ('40', '40 horas semanais'),
    ]

    tipo_bolsa_choices = [
        ('Bolsista Superior', 'Bolsista Superior'),
        ('Bolsista Médio', 'Bolsista Médio'),
    ]

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    eixo = models.ForeignKey(Eixos, on_delete=models.PROTECT)
    cidade_atuacao = models.CharField(max_length=50, choices=cidades_choices)
    carga_horaria = models.CharField(max_length=50, choices=carga_horaria_choices)
    tipo_bolsa = models.CharField(max_length=50, choices=tipo_bolsa_choices)
