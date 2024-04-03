import pytest
from pages.HomePage import HomePage  # Importando a classe 'HomePage'
from pages.LoginPage import LoginPage  # Importando a classe 'LoginPage'


@pytest.mark.usefixtures("setup_teardown")  # Usa a fixture "setup_teardown"
class TestCT01:
    def test_ct01_login_valido(self):

        # Instancia as classes a serem usadas no teste
        login_page = LoginPage()  # Atribuindo a classe 'LoginPage' na variável 'login_page'
        home_page = HomePage()  # Atribuindo a classe 'HomePage' na variável 'home_page'

        # Faz Login
        login_page.fazer_login("standard_user", "secret_sauce")
        # Da classe 'LoginPage' usar a função 'fazer_login' enviando os parâmetros usuário e senha

        # Verifica se login foi realizado
        home_page.verificar_login_com_sucesso()
        # Da classe 'HomePage' usar a função 'verificar_login_com_sucesso'

