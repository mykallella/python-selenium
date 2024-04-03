import conftest
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CheckoutPage(BasePage):  # Subclasse -> 'CarrinhoPage' Herda da 'BasePage'

    # Construtor
    def __init__(self):
        self.driver = conftest.driver  # Usando do arquivo 'conftest' a variável 'driver'

        # Locators
        self.campo_primeiro_nome = (By.ID, "first-name")
        self.campo_ultimo_nome = (By.ID, "last-name")
        self.campo_codigo_postal = (By.ID, "postal-code")
        self.botao_continue = (By.ID, "continue")
        self.botao_finish = (By.ID, "finish")
        self.mensagem_compra_realizada = (By.XPATH, "//*[text()='Thank you for your order!']")

    def realizar_compra(self, primeiro_nome, ultimo_nome, codigo_postal):
        self.escrever(self.campo_primeiro_nome, primeiro_nome)
        self.escrever(self.campo_ultimo_nome, ultimo_nome)
        self.escrever(self.campo_codigo_postal, codigo_postal)
        self.clicar(self.botao_continue)
        self.clicar(self.botao_finish)
        self.verificar_se_elemento_existe(self.mensagem_compra_realizada)
