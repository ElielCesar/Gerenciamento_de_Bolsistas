from django.contrib.auth.models import Group

def menu_context(request):
    # Verifica se o usuário está no grupo 'Coordenadores'
    is_coordenador = request.user.groups.filter(name='Coordenadores').exists()
    is_bolsista = request.user.groups.filter(name='Bolsistas').exists()
    is_financeiro = request.user.groups.filter(name='Financeiro').exists()

    return {'is_coordenador': is_coordenador, 'is_bolsista': is_bolsista, 'is_financeiro': is_financeiro }
