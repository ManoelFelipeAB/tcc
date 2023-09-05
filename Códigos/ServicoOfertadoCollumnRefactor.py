import pandas as pd

db_2015_1019 = 'C:/Users/agentes/Documents/Projeto HUC/dataset/resultados agosto/dbs_2015_nov2019.xlsx'

df_2022 = pd.read_excel(db_2015_1019)

# Supondo que a coluna que deseja alterar se chame 'coluna'
def adjust_values(val):
    val_str = str(val)
    if val_str.startswith("10"):
        return val_str[2:-4]  # Retira o "10" do início e o "00" do final
    else:
        return val_str[:-2]

df_2022['Servico Ofertado'] = df_2022['Servico Ofertado'].apply(adjust_values)

# x = 0
# for row in df_2022.iter_rows():
#     if x == 10:
#         break
#     print(row[2].value)
#     x+=1
# for cell in df_2022['Servico Ofertado']:
#     string = str(cell.value)
#     if string[0] != "1":
#         continue
#     else:
#         cell.value = string[2:len(string)-4]

# for i, row in df_2022.iterrows():
#     string = str(i)
#     if string[0] != "1":
#         continue
#     df_2022.loc[i,'Servico Ofertado']  = string[2:len(string)-4]


df_2022.to_excel(r'C:/Users/agentes/Documents/Projeto HUC/dataset/resultados agosto/db_final/db_2015_2019.xlsx', index=False)
