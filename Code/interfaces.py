from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
#Нужные изменения
'''from openpyxl import load_workbook

inv = load_workbook('../base_file/main.xlsx')

name_sheet = inv['Наименования']
items_for_combo_name = []


name_units = {'Выберите значение': ['Выберите значение'],
              'Амбулатория': ['АО1', 'АО2', 'АО3', 'АО4', 'КДЛ', 'Платное отделение'],
              'Стационар' : ['Стационар'],
              'Дневной Стационар': ['ДС1', 'ДС2', 'ДС3', 'ДС4'],
              'Вне плана': ['АО1', 'АО2', 'АО3', 'АО4', 'КДЛ',
                            'Платное отделение','Стационар','ДС1', 'ДС2', 'ДС3', 'ДС4']}


def unit_selected(self, value):
    items_for_combo = []
    for name, count in inv[value].values:
        if count != 0 and type(count) == int:
            items_for_combo.append(name)
    self.comboBox_subuint.clear()
    self.comboBox_name.addItems(items_for_combo)
    self.comboBox_subuint.clear()
    self.comboBox_subuint.addItems(name_units[value])

self.comboBox_unit.addItems(list(name_units.keys()))
self.comboBox_unit.currentTextChanged.connect(self.unit_selected)

'''
