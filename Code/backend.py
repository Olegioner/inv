from openpyxl import load_workbook


inv = load_workbook('../base_file/main.xlsx')

name_sheet = inv['Наименования']
moving_sheet = inv['Движение']


