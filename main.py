import pandas as pd
from utils.process_phone_numbers_sheet import process_phone_numbers_sheet
from utils.send_message import send_message


relatorio_nao_fizeram_provas = process_phone_numbers_sheet()
contatos_df = pd.DataFrame(relatorio_nao_fizeram_provas)
contatos_df.to_excel('nao_realizaram_provas.xlsx', index=False)
dados_df = pd.read_excel('nao_realizaram_provas.xlsx')
send_message(dados_df)
