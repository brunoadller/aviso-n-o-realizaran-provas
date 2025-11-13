import pandas as pd

def process_phone_numbers_sheet():
    #LENDO CSV DOS ARQUIVOS DE CADA POLO 
    polo1 = pd.read_csv('POLO1-TESTE.csv', sep=';',dtype={'MATRICULA': str})
    polo2 = pd.read_csv('POLO2-TESTE.csv', sep=';',dtype={'MATRICULA': str})
    polo3 = pd.read_csv('POLO3-TESTE.csv', sep=';',dtype={'MATRICULA': str})
    #junta os três polos em uma única planilha
    conjunto_polos = pd.concat([polo1,polo2,polo3], ignore_index=False)

    #LENDO XLSX DOS ALUNOS QUE NÃO FIZERAM PROVAS
    relatorio_provas_nao_realizadas = pd.read_excel('data.xlsx', dtype={'Matricula Aluno': str})
    #REMOVE AS DUPLICATAS
    clean_relatorio_provas_nao_realizadas = relatorio_provas_nao_realizadas.drop_duplicates(subset=['Matricula Aluno'])

    #COMPARA O NÚMERO DE MATRÍCULA E SE FORA IGUAL COLOCA NESTA NOVA LISTA DE DICIONÁRIOS
    relatorio_telefone_nao_provas = []
    for index, row_polos in conjunto_polos.iterrows():
        for index, row_provas in clean_relatorio_provas_nao_realizadas.iterrows():
            if(row_polos['MATRICULA'] == row_provas['Matricula Aluno']):
                relatorio_telefone_nao_provas.append({'Matricula': row_polos['MATRICULA'], 'telefone': row_polos['FONE_CELULAR']})
    return relatorio_telefone_nao_provas