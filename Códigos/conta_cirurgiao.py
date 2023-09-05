import csv
import pandas as pd
import funcoes_colunas

caminho_xlsx_saida = r'C:/Users/agentes/Documents/Projeto HUC/dataset/tcc/arqs/dataset_final.xlsx'

df = pd.read_excel(caminho_xlsx_saida)

print(df['Nome do cirurgiao'].unique())
print(df['Nome do cirurgiao'].nunique())

