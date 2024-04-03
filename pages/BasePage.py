import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:  # Classe Pai

    # Construtor
    def __init__(self):
        self.driver = conftest.driver  # Usando do arquivo 'conftest' a variável 'driver'

    def encontrar_elemento(self, locator):  # Recebe o locator como um pacote (By.ID, "user-name")
        return self.driver.find_element(*locator)  # Retorna => driver.find_element(By.ID, "user-name")
        # (*locator) => Desmembra o pacote

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        return self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    def pegar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text

    def esperar_elemento_aparecer(self, locator, timeout=10):  # Se não for recebido nenhum parâmetro para timeout, ele será 10
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
        # WebDriverWait(browser, 10).until(EC.alert_is_present())  # Espera até 10s o elemento aparecer

    def verificar_se_elemento_nao_existe(self, locator):
        # assert not self.encontrar_elementos(locator).is_displayed(), f"Esperado que o elemento '{locator}' não exista"
        assert len(self.encontrar_elementos(locator)) == 0, f"Esperado que elemento(s) {locator} não exista(m)."

    def clique_duplo(self, locator):
        elemento = self.esperar_elemento_aparecer(locator)  # Espera o elemento aparecer e também atribui o elemento retornado à variável 'elemento'
        ActionChains(self.driver).double_click(elemento).perform()

    def clique_botao_direito(self, locator):
        elemento = self.esperar_elemento_aparecer(locator)  # Espera o elemento aparecer e também atribui o elemento retornado à variável 'elemento'
        ActionChains(self.driver).context_click(elemento).perform()

    def teclar(self, locator, key):
        elemento = self.encontrar_elemento(locator)
        if key == "ENTER":
            elemento.send_keys(Keys.ENTER)
        elif key == "ESPACO":
            elemento.send_keys(Keys.SPACE)
        elif key == "F1":
            elemento.send_keys(Keys.F1)

