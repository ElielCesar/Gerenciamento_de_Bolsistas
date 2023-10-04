from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

# todos os testes devem passar, os testes que devem falhar precisam
# ser decorados com @pytest.mark.xfail

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


class Test_Menu_Bolsista(LiveServerTestCase):
    
    def setUp(self):
        self.webdriver = webdriver.Chrome()
        self.webdriver.get('http://127.0.0.1:8000/login/')
        self.campo_username = self.webdriver.find_element(By.ID, 'id_username')
        self.campo_password = self.webdriver.find_element(By.ID, 'id_password')
        self.botao_submit = self.webdriver.find_element(By.XPATH,
                '/html/body/div/main/div/div/form/button')
        self.campo_username.send_keys('111')
        self.campo_password.send_keys('1234')
        self.botao_submit.click()
        
    def tearDown(self):
        self.webdriver.close()

    def test_menu_pagamentos(self):
        menu_pagamentos = self.webdriver.find_element(By.CLASS_NAME, 'sidebar-link')
        assert menu_pagamentos.is_displayed()

    def test_submenu_solicitar(self):
        submenu_solicitar = self.webdriver.find_element(By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[2]/a')
        assert submenu_solicitar.is_displayed()

    def test_submenu_listar(self):
        submenu_listar = self.webdriver.find_element(By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[3]/a')
        assert submenu_listar.is_displayed()

    def test_menu_sair(self):
        menu_sair = self.webdriver.find_element(By.XPATH, '//*[@id="sidebar"]/div/ul/li[3]/a')
        assert menu_sair.is_displayed()

    def test_autorizar_pagamentos(self):
        item_menu = self.webdriver.find_element(By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[1]/a')

        item_menu.click()
        texto_da_pagina = self.webdriver.find_element(By.TAG_NAME, 'h1').text

        assert 'Not Found' in texto_da_pagina

    def test_solicitar_pagamentos(self):
        item_menu = self.webdriver.find_element(By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[2]/a')

        item_menu.click()
        formulario = self.webdriver.find_element(By.CLASS_NAME, 'form')

        assert formulario.is_displayed()

    def test_listar_pagamentos(self):
        item_menu = self.webdriver.find_element(By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[3]/a')

        item_menu.click()
        formulario = self.webdriver.find_element(By.CLASS_NAME, 'table')

        assert formulario.is_displayed()
