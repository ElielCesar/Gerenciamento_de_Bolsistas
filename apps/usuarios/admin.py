from django.contrib import admin
from apps.usuarios.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UsuariosAdmin(UserAdmin):
    model = Usuarios
    fieldsets = (
        (None, {'fields':('username', 'password')}),
        ('Dados Pessoais', {'fields':('cpf','first_name', 'last_name', 'email')}),
        ('Dados de Bolsista', {'fields':('carga_horaria', 'tipo_bolsa')}),
        ('Permissões', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

admin.site.register(Usuarios, UsuariosAdmin)