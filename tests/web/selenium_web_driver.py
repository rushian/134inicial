# Configura
# Dados de entrada
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

#[COMENTADO POR TER  SE TORNADO DINAMICO]  origem = 'São Paolo'
#[COMENTADO POR TER  SE TORNADO DINAMICO]  destino = 'New York'
primeiro_nome = 'Luca'
bandeira = 'American Express'
lembrar_de_mim = True
# resultados esperados
#[COMENTADO POR TER  SE TORNADO DINAMICO] titulo_passagens_esperado = 'Flights from São Paolo to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'


# Executa
class Testes:
    # inicio [SETUP COMENTADO PARA RODAR EM 2 NAVEGADORES DIFERENTES]
    # def setup_method(self):
    # instanciar engine
    #   self.driver = webdriver.Chrome()


    def teardown_method(self):
        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    # lista para uso como massa de teste
    lista_de_valores = [
        ('São Paolo', 'New York', 'firefox'),
        ('Boston', 'New York', 'chrome'),
        ('San Diego', 'New York', 'firefox')
    ]

    @pytest.mark.parametrize('origem,destino,browser', lista_de_valores)
    def testar_comprar_passagem(self, origem, destino, browser):
        # e2e / end to end / ponta a ponta
        print(browser)
        # Trouxe o setup_method / Iniciação para cá
        match browser:
            case 'chrome':
                self.driver = webdriver.Chrome()
            case 'firefox':
                options = Options()
                options.binary_location = r'C:\Users\Luciano\AppData\Local\Mozilla Firefox\firefox.exe'
                self.driver = webdriver.Firefox(options=options)

        # Pagina Inicial (Home)
        # Executa / Valida
        # abrir o browser no endereco
        self.driver.get('https://www.blazedemo.com')
        # clicar na lista de cidades de origem
        lista = self.driver.find_element(By.NAME, "fromPort")
        lista.click()
        # selecionar a cidade de origem desejada
        lista.find_element(By.XPATH, f'//option[ .= "{origem}"]').click()

        # clicar na lista de cidades de destino
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()

        # selecionar a cidade de destino desejada
        lista.find_element(By.XPATH, f'//option[ .= "{destino}"]').click()

        # clicar no botão de procurar voos
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

        # Pagina Lista de Passagens
        # Executa / Valida
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == f'Flights from {origem} to {destino}:'

        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(3)
        # Pagina de Compra
        # Executa / Valida
        # Limpar o campo do nome para evitar problemas ao digitar
        self.driver.find_element(By.ID, 'inputName').clear()
        # Prenche o nome do comprador
        self.driver.find_element(By.ID, 'inputName').send_keys(primeiro_nome)

        # Seleciona a bandeira do cartao
        lista = self.driver.find_element(By.ID, 'cardType')
        lista.click()
        lista.find_element(By.XPATH, f'//option[ .= "{bandeira}"]').click()

        # Marca o checkbox para ser lembrado
        self.driver.find_element(By.ID, 'rememberMe').click()
        time.sleep(3)
        # Aperta o botao Purchase Flight
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

        # Pagina de Obrigado
        # Valida
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == mensagem_agradecimento_esperada
        assert self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(2)').text == \
               preco_passagem_esperado
        time.sleep(3)


'''
    # Meio
    def testar_comprar_passagem_by_jeferson(self):

        # e2e / end to end / ponta a ponta
        # Pagina Inicial (Home)
        # Executa / Valida
        # abrir o browser no endereço
        self.driver.get('https://www.blazedemo.com')
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Welcome to the Simple Travel Agency!"
        lista = self.driver.find_element(By.NAME, 'fromPort')
        lista.click()
        # selecionar cidade de origen
        lista.find_element(By.XPATH, f'//option[ .= "{origem}" ]').click()
        # clicar na lista de cidade de destino
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()
        # selecionar cidade de origen
        lista.find_element(By.XPATH, f'//option[ .= "{destino}" ]').click()

        # cliar no botao procurar voos
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == f'Flights from "{origem}" to "{destino}":'
        time.sleep(3)
        # Pagina Lista de Passagens
        # Executa / Valida
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == titulo_passagens_esperado
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(6)").text == "Price"
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()


        # for preco in precos:
        #     print(preco.text)

        # Pagina de Compra

        # Executa / Valida
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Your flight from TLV to SFO has been reserved."
        self.driver.find_element(By.ID, "inputName").click()
        self.driver.find_element(By.ID, "inputName").send_keys("Aula134")
        self.driver.find_element(By.ID, "address").click()
        self.driver.find_element(By.ID, "address").send_keys("rua")
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.ID, "city").send_keys("goiania")
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.ID, "state").send_keys("go")
        self.driver.find_element(By.ID, "zipCode").click()
        self.driver.find_element(By.ID, "zipCode").send_keys("12345")
        self.driver.find_element(By.ID, "cardType").click()
        dropdown = self.driver.find_element(By.ID, "cardType")
        dropdown.find_element(By.XPATH, "//option[. = 'American Express']").click()
        self.driver.find_element(By.ID, "creditCardNumber").click()
        self.driver.find_element(By.ID, "creditCardNumber").send_keys("2222222222221111")
        self.driver.find_element(By.ID, "creditCardMonth").click()
        self.driver.find_element(By.ID, "creditCardYear").click()
        self.driver.find_element(By.ID, "nameOnCard").click()
        self.driver.find_element(By.ID, "nameOnCard").send_keys("teseeeee")
        self.driver.find_element(By.ID, "rememberMe").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        # Pagina de Obrigado
        # Executa

        # Valida
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thank you for your purchase today!"
'''
