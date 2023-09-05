import csv
import openpyxl
import string

def clean_data(data):
    printable = set(string.printable)
    return ''.join(filter(lambda x: x in printable, data))

def csv_to_excel(csv_filename, excel_filename):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    with open(csv_filename, 'r', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            cleaned_row = [clean_data(cell) for cell in row]
            sheet.append(cleaned_row)

    workbook.save(excel_filename)
    print(f"CSV file '{csv_filename}' converted to Excel file '{excel_filename}'.")

if __name__ == "__main__":
    csv_filename = "//arqs/jan2015_nov2019.csv"
    excel_filename = "//arqs/teste.xlsx"
    csv_to_excel(csv_filename, excel_filename)
