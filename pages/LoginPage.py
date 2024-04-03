import conftest
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):  # Subclasse -> 'LoginPage' Herda da 'BasePage'

    # Construtor
    def __init__(self):
        self.driver = conftest.driver  # Usando do arquivo 'conftest' a variável 'driver'

        # Locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.erro_login = (By.XPATH, "//*[@data-test='error']")
        self.erro_login_texto = (By.XPATH, "//*[contains(text(), 'Epic sadface: Username and password do not match any user in this service')]")

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verificar_login_invalido(self):
        self.verificar_se_elemento_existe(self.erro_login)

    def verificar_login_invalido_texto_fixo(self):
        self.verificar_se_elemento_existe(self.erro_login_texto)

    def verificar_login_invalido_texto_esperado(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.erro_login)
        assert texto_encontrado == texto_esperado, f"Texto encontrado'{texto_encontrado}'. Texto esperado: '{texto_esperado}'"

