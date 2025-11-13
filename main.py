import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from  process_phone_numbers_sheet import process_phone_numbers_sheet


relatorio_nao_fizeram_provas = process_phone_numbers_sheet()

contatos_df = pd.DataFrame(relatorio_nao_fizeram_provas)
contatos_df.to_excel('nao_realizaram_provas.xlsx', index=False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager))
driver.get('https://web.whatsapp.com')



dados = pd.read_excel('nao_realizaram_provas.xlsx')

for index, row in dados.iterrows():
    numero = str(row['Telefone'])