import pytest
from pages.CarrinhoPage import CarrinhoPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")  # Usa a fixture "setup_teardown"
@pytest.mark.carrinho  # Marcador 'carrinho'
class TestCT03:
    def test_ct03_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        checkout_page = CheckoutPage()

        produto_1 = 'Sauce Labs Backpack'
        produto_2 = 'Sauce Labs Bike Light'

        # Fazendo Login
        login_page.fazer_login('standard_user', 'secret_sauce')

        # Adicionando a mochila ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # Verificando que a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Clicando no botão 'Continue Shopping' (voltando para a Home)
        carrinho_page.continuar_comprando()

        # Adicionando mais um produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        # Verificando que os 2 produtos estão no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

        # Fazendo a compra dos 2 produtos
        carrinho_page.acessar_checkout()
        checkout_page.realizar_compra('Myrela', 'Barros', '12425190')
