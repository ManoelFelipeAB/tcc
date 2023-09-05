import csv
import pandas as pd
import funcoes_colunas
# Caminho do arquivo CSV de entrada
caminho_csv = 'C:/Users/agentes/Documents/Projeto HUC/dataset/datasets merged/jan2015_nov2019.csv'

# Caminho do arquivo CSV de saída com colunas adicionadas
caminho_csv_saida = 'C:/Users/agentes/Documents/Projeto HUC/dataset/tcc/arqs/database2015_2019.csv'

# Lê o arquivo CSV existente
linhas = []
with open(caminho_csv, 'r', newline='', encoding='latin-1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=';')
    for linha in leitor_csv:
        #print(linha)
        linhas.append(linha)

# Adiciona as colunas 'ID', 'Mês' e 'Ano' ao cabeçalho
linhas[0].extend(['ID', 'Mês', 'Ano'])

# Adiciona os valores nas linhas
for i, linha in enumerate(linhas[1:], start=1):
    if 1 <= i <= 11249:
        funcoes_colunas.ano_2015(i, linha)
    elif 11251 <= i <= 22537:
        funcoes_colunas.ano_2016(i, linha)
    elif 22539 <= i <= 33140:
        funcoes_colunas.ano_2017(i, linha)
    elif 33142 <= i <= 45357:
        funcoes_colunas.ano_2018(i, linha)
    elif 45359 <= i <= 57746:
        funcoes_colunas.ano_2019(i, linha)
    else:
        continue


        #linha.extend([str(i), 'Março', '2015'])

# Escreve os dados atualizados no novo arquivo CSV
with open(caminho_csv_saida, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    escritor_csv.writerows(linhas)

print('Colunas adicionadas e arquivo CSV salvo com sucesso.')

# Ler o novo arquivo CSV utilizando a biblioteca pandas
dados = pd.read_csv(caminho_csv_saida, delimiter=';')
print(dados.head())

# linhas_nome_da_coluna = [828, 1652, 2631, 3582, 4545, 5471, 6415, 7366, 8327, 9393, 10359,
#                          11251, 12098, 12996, 14014, 14996, 16025, 17042, 18051, 18998,
#                          19879, 20767, 21639, 22539, 23280, 23920, 24788, 25614, 26592,
#                          27475, 28407, 29395, 30347, 31326, 32303, 33142, 33880, 34744,
#                          35758, 36805, 37926, 38976, 40145, 41364, 42363, 43373, 44414,
#                          45359, 46352, 47437, 48554, 49765, 50910, 51955, 53126, 54303,
#                          55478, 56691]
#
#
# for linha in linhas_nome_da_coluna:
#     funcoes_colunas.apagar_linha_csv('database2015_2019.csv', linha)
