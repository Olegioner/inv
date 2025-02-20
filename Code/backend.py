from openpyxl import load_workbook
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

inv = load_workbook('../base_file/main.xlsx')

name_sheet = inv['Наименования']
moving_sheet = inv['Движение']


