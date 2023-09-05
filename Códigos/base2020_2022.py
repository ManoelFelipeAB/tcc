import calendar

import pandas as pd

db = 'C:/Users/agentes/Documents/Projeto HUC/dataset/resultados agosto/db_final_2020_2022/dbs_2020_2022.xlsx'
df_original = pd.read_excel(db)
x = 0

for _, row in df_original.iterrows():
    lista = str(df_original.at[x,'DT. AGENDAMENTO'])[:10].split("-")
    df_original.at[x,'Mês'] = calendar.month_name[int(lista[1])]
    df_original.at[x,'Ano'] = lista[0]
    if x % 1000 == 0:
        print(x)
    x+=1




df_repeated = pd.concat([df_original] * 4, ignore_index=True)

df_sorted = df_repeated.sort_values(by='CIRURGIA').reset_index(drop=True)

columns = ['INICIO ANESTESIA', 'INICIO PROC. CIRURGICO', 'TERMINO PROC. CIRURGICO', 'TERMINO ANESTESIA']

x = 0

for _, row in df_sorted.iterrows():
    if x % 4 == 0:
        df_sorted.at[x, 'Atividade'] = 'INICIO ANESTESIA'
        df_sorted.at[x, 'Timestamp'] = row['INICIO ANESTESIA']
    elif x % 4 == 1:
        df_sorted.at[x, 'Atividade'] = 'INICIO PROC. CIRURGICO'
        df_sorted.at[x, 'Timestamp'] = row['INICIO PROC. CIRURGICO']
    elif x % 4 == 2:
        df_sorted.at[x, 'Atividade'] = 'TERMINO PROC. CIRURGICO'
        df_sorted.at[x, 'Timestamp'] = row['TERMINO PROC. CIRURGICO']
    elif x % 4 == 3:
        df_sorted.at[x, 'Atividade'] = 'TERMINO ANESTESIA'
        df_sorted.at[x, 'Timestamp'] = row['TERMINO ANESTESIA']
    x+=1
    if x % 1000 == 0:
        print(x)

data = {
    'ID_CIRURGIA': df_sorted['CIRURGIA'] ,
    'ID_PACIENTE': df_sorted['ATENDIMENTO'],
    'MÊS': df_sorted['Mês'],
    'ANO': df_sorted['Ano'],
    'IDADE': df_sorted['Idade'],
    'PRIORIDADE': df_sorted['CLASSIFICAÇÃO AGENDA'],
    'COMPLEXIDADE': df_sorted['COMPLEXIDADE?'],
    'SALA': df_sorted['SALA'],
    'STATUS_CIRURGIA': df_sorted['STATUS CIRURGIA'],
    'ID_PROCEDIMENTO': df_sorted['PROC. PRINCIPAL'],
    'ANESTESISTA': df_sorted['ANESTESISTA'],
    'ID_CIRURGIAO': df_sorted['CIRURGIAO'],
    'OBSERVAÇÃO': df_sorted['OBSERVACAO'],
    'ATIVIDADE': df_sorted['Atividade'],
    'TIMESTAMP': df_sorted['Timestamp']
}

df_ml = pd.DataFrame(data)



df_ml.to_excel(r'C:/Users/agentes/Documents/Projeto HUC/dataset/resultados agosto/db_final_2020_2022/db_2020_2022_FINAL.xlsx', index=False)