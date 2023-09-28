from django.db import models
from apps.bolsistas.models import Bolsista
from django.core.validators import FileExtensionValidator

# Create your models here.
class Relatorio(models.Model):
    mes_choice = [
        # banco       usuario
        ('Janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro'),
    ]

    ano_choice = [
        (2020, '2020'),
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
    ]

    situacao_choices = [
        ('pago', 'pago'),
        ('recusado', 'recusado'),
        ('aguardando', 'aguardando'),
    ]

    bolsista = models.ForeignKey(Bolsista, on_delete=models.DO_NOTHING)
    mes = models.CharField(max_length=30, choices=mes_choice)
    ano = models.PositiveIntegerField(choices=ano_choice)
    valor_bolsa = models.DecimalField(max_digits=8, decimal_places=2)
    relatorio = models.FileField(
        upload_to='relatorios/',
        verbose_name='Relatório em PDF', 
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        )
    
    situacao = models.CharField(
        max_length=15,
        choices=situacao_choices,
        default='aguardando',
        verbose_name="Situacão")
    
    comprovante_pagamento = models.FileField(
        upload_to='comprovantes_pagamento/',
        verbose_name='Comprovante de Pag. - Reservado para o setor Financeiro',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f'{self.bolsista.nome}'


