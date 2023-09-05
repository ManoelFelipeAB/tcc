import pandas as pd

df_2020 = pd.read_excel('DB/Original_Anonimizada/Dataset_2020_Original_Anonimizada.xlsx')
df_2021 = pd.read_excel('DB/Original_Anonimizada/Dataset_2021_Original_Anonimizada.xlsx')
df_2022 = pd.read_excel('DB/Original_Anonimizada/Dataset_2022_Original_Anonimizada.xlsx')

result = pd.concat([df_2020, df_2021, df_2022], ignore_index=True)

result.to_excel('DB/DB_2020_2022/Merge/Dataset_2020_2022_merged.xlsx', index=False)
