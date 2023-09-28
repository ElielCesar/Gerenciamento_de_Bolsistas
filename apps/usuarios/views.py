# vai puxar a var que redireciona para tela inicial
from django.conf import settings  
from apps.usuarios.forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    authentication_form = CustomAuthenticationForm
    success_url = '/sistema/'