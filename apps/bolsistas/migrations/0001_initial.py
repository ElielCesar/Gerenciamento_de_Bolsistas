# Generated by Django 4.2.5 on 2023-09-27 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eixos', '0002_alter_eixos_cidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolsista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('cidade_atuacao', models.CharField(choices=[('Ariquemes', 'Ariquemes'), ('Porto Velho', 'Porto Velho'), ('Alto Alegre', 'Alto Alegre'), ('Buritis', 'Buritis'), ('Cerejeiras', 'Cerejeiras'), ('Pimenta Bueno', 'Pimenta Bueno')], max_length=50)),
                ('carga_horaria', models.CharField(choices=[(20, '20 horas semanais'), (30, '30 horas semanais'), (40, '40 horas semanais')], max_length=50)),
                ('tipo_bolsa', models.CharField(choices=[('BS', 'Bolsista Superior'), ('BM', 'Bolsista Médio')], max_length=50)),
                ('eixo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eixos.eixos')),
            ],
        ),
    ]
