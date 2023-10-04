from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

# todos os testes aqui devem passar
# caso seja necessário que ele falhe use @pytest.mark.xfail
class Test_Elementos_Login_Page(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/login/')

    def test_titulo_existe(self):
        assert self.driver.title == 'Login'

    def test_logo_projeto_existe(self):
        # Testa a presença da imagem no elemento
        imagem = self.driver.find_element(By.XPATH, '//*[@id="sidebar"]/div/div/a/img')
        assert imagem.is_displayed()

    def test_imagem_login_existe(self):
        # testa se a imagem no form de login existe
        imagem = self.driver.find_element(By.XPATH, '/html/body/div/main/div/img')
        assert imagem.is_displayed()

    def test_form_login_existe(self):
        formulario = self.driver.find_element(By.TAG_NAME, 'form')
        assert formulario.is_displayed()

    def tearDown(self):
        self.driver.close()

class Test_User_Login(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/login/')
        self.campo_usuario = self.driver.find_element(By.ID, 'id_username')
        self.campo_senha = self.driver.find_element(By.ID, 'id_password')
        self.botao_enviar = self.driver.find_element(By.XPATH, '/html/body/div/main/div/div/form/button')

    def test_login_bolsista(self):
        self.campo_usuario.send_keys('111')
        self.campo_senha.send_keys('1234')
        self.botao_enviar.click()

        assert self.driver.title == 'Sistema'

    def test_login_coordenador(self):
        self.campo_usuario.send_keys('444')
        self.campo_senha.send_keys('1234')
        self.botao_enviar.click()

        assert self.driver.title == 'Sistema'

    def test_login_financeiro(self):
        self.campo_usuario.send_keys('666')
        self.campo_senha.send_keys('1234')
        self.botao_enviar.click()

        assert self.driver.title == 'Sistema'

    def tearDown(self):
        self.driver.close()
