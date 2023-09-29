# verificam se o usuário logado faz parte do grupo criado no django admin

def is_bolsista(user):
    return user.groups.filter(name='Bolsistas').exists()

def is_coordenador(user):
    return user.groups.filter(name='Coordenadores').exists()

def is_financeiro(user):
    return user.groups.filter(name='Financeiro').exists()
