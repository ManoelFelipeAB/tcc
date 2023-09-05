import openpyxl

caminho_xlsx_saida = r'C:/Users/agentes/Documents/Projeto HUC/dataset/tcc/arqs/data_atual_arrumado_2.xlsx'

linhas_nome_da_coluna = [2626, 2627, 2628, 27445]

# Load the workbook and select the active sheet
workbook = openpyxl.load_workbook(caminho_xlsx_saida)
sheet = workbook.active

# Iterate through the rows in reverse (so that deleting rows doesn't affect the indices of subsequent rows)
for index in sorted(linhas_nome_da_coluna, reverse=True):
    sheet.delete_rows(index)

# Save the changes back to the original file
workbook.save(caminho_xlsx_saida)

print("Lines removed from the original .xlsx file!")
