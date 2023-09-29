# # script para gerenciar grupos de usuarios

# from django.db import migrations
# from django.contrib.auth.models import Group, Permission
# from apps.bolsistas.models import Bolsista
# from apps.eixos.models import Eixos
# from apps.pagamentos.models import Relatorio

# def create_groups(apps, schema_editor):
#     # meus grupos
#     bolsistas_group, _= Group.objects.get_or_create(name='Bolsistas')
#     coordenadores_group, _= Group.objects.get_or_create(name='Coordenadores')
#     financeiro_group, _= Group.objects.get_or_create(name='Financeiro')

#     # permissões de cada grupo
#     bolsistas_group.permissions.add(
#         Permission.objects.get(codename='view_eixo'),
#         Permission.objects.get(codename='view_bolsista'),
#         Permission.objects.get(codename='add_pagamento'),
#         Permission.objects.get(codename='view_pagamento'),
#     )

#     coordenadores_group.permissions.add(
#         Permission.objects.get(codename='view_eixo'),
#         Permission.objects.get(codename='add_eixo'),
#         Permission.objects.get(codename='change_eixo'),
#         Permission.objects.get(codename='delete_eixo'),
#         Permission.objects.get(codename='view_bolsista'),
#         Permission.objects.get(codename='add_bolsista'),
#         Permission.objects.get(codename='change_bolsista'),
#         Permission.objects.get(codename='delete_bolsista'),
#         Permission.objects.get(codename='view_pagamento'),
#         Permission.objects.get(codename='add_pagamento'),
#     )

#     financeiro_group.permissions.add(
#         Permission.objects.get(codename='view_pagamento'),
#         Permission.objects.get(codename='add_pagamento'),
#         Permission.objects.get(codename='change_pagamento'),
#         Permission.objects.get(codename='delete_pagamento'),
#     )

# class Migration(migrations.Migration):

#     dependencies = []

#     operations = [
#         migrations.RunPython(create_groups)
#     ]
















