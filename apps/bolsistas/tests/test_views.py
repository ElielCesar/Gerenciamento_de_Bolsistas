from django.urls import reverse
from django.contrib.auth.models import Group
from django.test import TestCase
from apps.usuarios.models import Usuarios

class Test_Cadastrar_Bolsista(TestCase):

    def setUp(self):
        # usuario de teste
        self.user = Usuarios.objects.create_user(
            username='777',
            password='1234',
            email='teste777@gmail.com',
            cpf='777',
            carga_horaria=20,
            tipo_bolsa='Bolsista Superior'
        )

        grupo_coordenadores = Group.objects.get(name='Coordenadores')
        self.user.groups.add(grupo_coordenadores)

    # autenticacao e permissao
    def test_autenticacao_requerida(self):
        response = self.client.get(reverse('cadastrar_bolsistas'))
        self.assertEqual(response.status_code, 302)

    def test_acesso_permissoes(self):
        self.client.login(username='777', password='1234')
        response = self.client.get(reverse('cadastrar_bolsistas'))
        self.assertEqual(response.status_code, 200)

    # testes para o formulario
    def test_formulario_correto(self):
        self.client.login(username='777', password='1234')
        dados = {
            'nome':'bolsistatestecase',
            'cpf':'12341111',
            'eixo':'Saúde',
            'cidade_atuacao':'Ariquemes',
            'carga_horaria':'20 horas semanais',
            'tipo_bolsla':'Bolsista Superior',
            }
        response = self.client.post(reverse('cadastrar_bolsistas'), dados)
        self.assertEqual(response.status_code, 302)

    # def test_formulario_invalido(self):
    #     self.client.login(username='777', password='1234')
    #     dados = {'username':'111', 'password':'1234'}
    #     response = self.client.post(reverse('cadastrar_bolsistas'), dados)
    #     self.assertEqual(response.status_code, 200)
    