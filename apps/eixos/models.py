from django.db import models

# Create your models here.
class Eixos(models.Model):
    cidades_choices = [
        ('Ariquemes', 'Ariquemes'),
        ('Porto Velho', 'Porto Velho'),
        ('Alto Alegre', 'Alto Alegre'),
        ('Buritis', 'Buritis'),
        ('Cerejeiras', 'Cerejeiras'),
        ('Pimenta Bueno', 'Pimenta Bueno'),
    ]
    nome_eixo = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200, choices=cidades_choices)
    coordenador_eixo = models.CharField(max_length=200)
    objetivo_eixo = models.TextField()

    def __str__(self):
        return self.nome_eixo