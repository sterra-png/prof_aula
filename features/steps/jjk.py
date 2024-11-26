from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Importando a classe Service
from webdriver_manager.chrome import ChromeDriverManager  # Usando o WebDriver Manager para automatizar o download do chromedriver
import time

# Passo: Garantir que o ChromeDriver seja obtido corretamente
@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    # Usando o ChromeDriverManager para obter o chromedriver mais recente
    service = Service(ChromeDriverManager().install())  # Instala e configura automaticamente o chromedriver
    context.driver = webdriver.Chrome(service=service)  # Inicializa o navegador com o chromedriver
    context.driver.get('https://www.jogajuntoinstituto.org/')

@when(u'Insiro meus dados')
def step_impl(context):
    context.driver.find_element(By.ID, 'nome').send_keys('felipe')
    context.driver.find_element(By.ID, 'email').send_keys('bhachbasbfysbade')
    context.driver.find_element(By.ID, 'assunto').send_keys(Keys.ARROW_DOWN, Keys.TAB)

@when(u'Envio a mensagem "Olá da turma de QA Avançado, Ilhabela Novembro 2024"')
def step_impl(context):
    context.driver.find_element(By.ID, 'mensagem').send_keys('tamo junto ai')
    botao_enviar = context.driver.find_element(By.XPATH, '//*[@id="Contato"]/div[1]/form/button')
    botao_enviar.submit()

@then(u'Fecho o navegador')
def step_impl(context):
    time.sleep(5)
    context.driver.quit()
print('ola')