# Generated by Django 4.2.5 on 2023-09-28 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsistas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolsista',
            name='carga_horaria',
            field=models.CharField(choices=[('20', '20 horas semanais'), ('30', '30 horas semanais'), ('40', '40 horas semanais')], max_length=50),
        ),
    ]
