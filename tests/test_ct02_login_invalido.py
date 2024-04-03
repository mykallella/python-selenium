import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_teardown")  # Usa a fixture "setup_teardown"
class TestCT02:
    def test_ct02_login_invalido(self):

        # Atributos
        erro_esperado = "Epic sadface: Username and password do not match any user in this service"

        # Instancia as classes a serem usadas no teste
        login_page = LoginPage()
        home_page = HomePage()

        # Tenta Login Inválido
        login_page.fazer_login('standard_user', 'senha_incorreta')

        # Verifica se login não foi realizado
        login_page.verificar_login_invalido()

        # Verifica se login não foi realizado e se a mensagem apareceu
        login_page.verificar_login_invalido_texto_fixo()

        # Verifica se login não foi realizado e se a mensagem X apareceu
        login_page.verificar_login_invalido_texto_esperado(erro_esperado)

