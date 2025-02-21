from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
#Нужные изменения
'''inv = load_workbook('../base_file/main.xlsx')

# name_sheet = inv['Наименования']
# items_for_combo_name = []
#
# for name, count in name_sheet.values:
#     if count != 0 and type(count) == int:
#         items_for_combo_name.append(name)

name_units = {'Амбулатория': ['АО1', 'АО2', 'АО3', 'АО4', 'КДЛ', 'ПЦР', 'Платное отделение'],
              'Стационар' : ['ДО', 'ВО', 'ДДО'],
              'Дневной Стационар': ['ДС1', 'ДС2', 'ДС3', 'ДС4']}

def unit_selected(self, value):
    items_for_combo = []
    for name, count in inv[value].values:
        if count != 0 and type(count) == int:
            items_for_combo.append(name)
    self.comboBox_name.addItems(items_for_combo)



self.comboBox_unit.addItems(list(name_units.keys()))
self.comboBox_unit.currentTextChanged.connect(self.unit_selected)

'''