import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver: webdriver.Remote  # Variável global


@pytest.fixture  # Define que a função abaixo é uma fixture
def setup_teardown():
    # Setup
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Conecta ao browser
    driver.implicitly_wait(5)  # Espera toda ação até 5s
    driver.maximize_window()  # maximiza a janela
    driver.get("https://www.saucedemo.com/")  # Acessa a página

    # run test
    yield  # Pula para onde essa função "setup_teardown()" foi chamada e continua executando lá, depois volta.

    # teardown
    driver.quit()

