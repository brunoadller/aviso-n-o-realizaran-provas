import pandas as pd
import time
from utils.process_phone_numbers_sheet import process_phone_numbers_sheet
from utils.message import message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib


relatorio_nao_fizeram_provas = process_phone_numbers_sheet()
contatos_df = pd.DataFrame(relatorio_nao_fizeram_provas)
contatos_df.to_excel('nao_realizaram_provas.xlsx', index=False)
dados_df = pd.read_excel('nao_realizaram_provas.xlsx')



navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com')


while len(navegador.find_elements(By.ID,"side")) < 1:
    time.sleep(1)
    #já foi feito o login no web
    for i, row in dados_df.iterrows():
        nome = row['Nome']
        telefone = row['Telefone']
        texto = urllib.parse.quote(f"Olá {nome}, tudo bem?\nSó informando que estou passando aqui para testar o envio de mensagens.")
        link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
        navegador.get(link)
        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(1)
            campo = WebDriverWait(navegador, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
                )
            campo.send_keys(Keys.ENTER)
            time.sleep(10)