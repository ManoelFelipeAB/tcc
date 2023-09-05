import openpyxl

caminho_xlsx_saida = r'C:/Users/agentes/Documents/Projeto HUC/dataset/tcc/arqs/data_atual_arrumado.xlsx'

linhas_nome_da_coluna = [828, 1652, 2631, 3582, 4545, 5471, 6415, 7366, 8327, 9393, 10359,
                         11251, 12098, 12996, 14014, 14996, 16025, 17042, 18051, 18998,
                         19879, 20767, 21639, 22539, 23280, 23920, 24788, 25614, 26592,
                         27475, 28407, 29395, 30347, 31326, 32303, 33142, 33880, 34744,
                         35758, 36805, 37926, 38976, 40145, 41364, 42363, 43373, 44414,
                         45359, 46352, 47437, 48554, 49765, 50910, 51955, 53126, 54303,
                         55478, 56691]

# Load the workbook and select the active sheet
workbook = openpyxl.load_workbook(caminho_xlsx_saida)
sheet = workbook.active

# Iterate through the rows in reverse (so that deleting rows doesn't affect the indices of subsequent rows)
for index in sorted(linhas_nome_da_coluna, reverse=True):
    sheet.delete_rows(index)

# Save the changes back to the original file
workbook.save(caminho_xlsx_saida)

print("Lines removed from the original .xlsx file!")
