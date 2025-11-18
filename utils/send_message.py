import time
from utils.message import message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib

def send_message(dados_df):
    # Abre navegador
    navegador = webdriver.Chrome()
    navegador.get('https://web.whatsapp.com')

    print("👉 Faça login no WhatsApp...")
    WebDriverWait(navegador, 60).until(
        EC.presence_of_element_located((By.ID, "side"))
    )
    print("✅ Login detectado!")

    for i, row in dados_df.iterrows():

        nome = row["Nome"]
        telefone = row["Telefone"]

        texto = urllib.parse.quote(
            f"Olá {nome}, tudo bem?\n"
            f"{message()}"
        )

        link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
        navegador.get(link)

        try:
            # espera abrir a conversa
            WebDriverWait(navegador, 30).until(
                EC.presence_of_element_located((By.ID, "main"))
            )

            # espera o campo de digitação REAL
            campo = WebDriverWait(navegador, 30).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//*[@id='main']//div[@role='textbox']"
                ))
            )

            # envia ENTER
            campo.send_keys(Keys.ENTER)

            print(f"✅ Mensagem enviada para {nome} ({telefone})")

            # tempo para evitar bloqueio
            time.sleep(5)
        except Exception as e:
            print(f"Erro ao processar o envio de mensagens {e} ")

    print("🚀 FINALIZADO!")
