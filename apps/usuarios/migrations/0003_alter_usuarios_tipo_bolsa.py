# Generated by Django 4.2.5 on 2023-10-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuarios_carga_horaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='tipo_bolsa',
            field=models.CharField(choices=[('Coordenador do Projeto', 'Coordenador do Projeto'), ('Coordenador do Eixo', 'Coordenador do Eixo'), ('Bolsista Superior', 'Bolsista Superior'), ('Bolsista Medio', 'Bolsista Medio')], max_length=100),
        ),
    ]
