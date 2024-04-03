import conftest
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):  # Subclasse -> 'HomePage' Herda da 'BasePage'

    # Construtor
    def __init__(self):
        self.driver = conftest.driver  # Usando do arquivo 'conftest' a variável 'driver'

        # Locators
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_inventario = (By.XPATH, "//div[@class='inventory_item_name ' and text()='{}']")
        self.botao_adicionar_ao_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        # item:
        # self.item_inventario[0] -> By.XPATH
        # self.item_inventario[1] -> "//div[@class='inventory_item_name ' and text()='{}']"
        # item = (By.XPATH, "//div[@class='inventory_item_name ' and text()='{}']".format(nome_item))
        # item = (By.XPATH, "//div[@class='inventory_item_name ' and text()='{nome_item}']"

        self.clicar(item)
        self.clicar(self.botao_adicionar_ao_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)

