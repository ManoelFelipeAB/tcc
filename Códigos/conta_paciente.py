import openpyxl


def generate_name_frequency_dict(xlsx_filename):
    name_frequency = {}

    workbook = openpyxl.load_workbook(xlsx_filename)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        patient_name = row[1]  # Assuming 'Nome do paciente' is the second column (index 1)
        if patient_name in name_frequency:
            name_frequency[patient_name] += 1
        else:
            name_frequency[patient_name] = 1

    return name_frequency


if __name__ == "__main__":
    xlsx_filename = "//arqs/database2015_2019.csv"
    name_frequency_dict = generate_name_frequency_dict(xlsx_filename)

    for name, frequency in name_frequency_dict.items():
        print(f"{name}: {frequency} occurrences")
