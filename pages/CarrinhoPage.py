import conftest
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CarrinhoPage(BasePage):  # Subclasse -> 'CarrinhoPage' Herda da 'BasePage'

    # Construtor
    def __init__(self):
        self.driver = conftest.driver  # Usando do arquivo 'conftest' a variável 'driver'

        # Locators
        self.item_inventario = (By.XPATH, "//div[@class='inventory_item_name' and text()='{}']")
        self.botao_continue_shopping = (By.ID, "continue-shopping")
        self.botao_checkout = (By.ID, "checkout")

    def verificar_produto_carrinho_existe(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        # item:
        # self.item_inventario[0] -> By.XPATH
        # self.item_inventario[1] -> "//div[@class='inventory_item_name ' and text()='{}']"
        # item = (By.XPATH, "//div[@class='inventory_item_name ' and text()='{}']".format(nome_item))
        # item = (By.XPATH, "//div[@class='inventory_item_name ' and text()='{nome_item}']"

        self.verificar_se_elemento_existe(item)

    def continuar_comprando(self):
        self.clicar(self.botao_continue_shopping)

    def acessar_checkout(self):
        self.clicar(self.botao_checkout)

