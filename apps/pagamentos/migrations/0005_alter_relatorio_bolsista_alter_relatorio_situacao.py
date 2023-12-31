# Generated by Django 4.2.5 on 2023-10-01 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolsistas', '0003_alter_bolsista_tipo_bolsa'),
        ('pagamentos', '0004_alter_relatorio_comprovante_pagamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='bolsista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bolsistas.bolsista'),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='situacao',
            field=models.CharField(choices=[('pago', 'pago'), ('recusado', 'recusado'), ('aguardando', 'aguardando')], default='aguardando', max_length=15, verbose_name='Situacão - Reservado para o setor Financeiro'),
        ),
    ]
