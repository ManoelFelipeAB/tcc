import pandas as pd

b1 = 'C:/Users/agentes/Documents/Projeto HUC/dataset/resultados agosto/dbs_2015_nov2019.xlsx'
b2 = 'C:/Users/agentes/Documents/Projeto HUC/dataset/resultados agosto/Dezembro - Tasy.xlsx'
b3 = 'C:/Users/agentes/Documents/Projeto HUC/dataset/resultados agosto/dbs_2020_2022.xlsx'

df_b1 = pd.read_excel(b1)
df_b2 = pd.read_excel(b2)
df_b3 = pd.read_excel(b3)

print("B1:")
print(len(df_b1.columns))
print(df_b1.columns.values.tolist())


print("B2:")
print(len(df_b2.columns))
print(df_b2.columns.values.tolist())

print("B3:")
print(len(df_b3.columns))
print(df_b3.columns.values.tolist())