from openpyxl import load_workbook
from PyQt5 import QtWidgets

import sys
import inv_interfaces
from openpyxl import load_workbook
from datetime import datetime

inv = load_workbook('../base_file/main.xlsx')

name_sheet = inv['Наименования']
moving_sheet = inv['Движение']
items_for_combo_name = []

name_units = {'Выберите значение': ['Выберите значение'],
              'Амбулатория': ['АО1', 'АО2', 'АО3', 'АО4', 'КДЛ', 'Платное отделение'],
              'Стационар' : ['Стационар'],
              'Дневной Стационар': ['ДС1', 'ДС2', 'ДС3', 'ДС4'],
              'Вне плана': ['АО1', 'АО2', 'АО3', 'АО4', 'КДЛ',
                            'Платное отделение','Стационар','ДС1', 'ДС2', 'ДС3', 'ДС4']}


class ExampleApp(QtWidgets.QMainWindow, inv_interfaces.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации дизайна

        self.comboBox_unit.addItems(list(name_units.keys()))
        self.comboBox_unit.currentTextChanged.connect(self.unit_selected)

        self.pushButton_into_values.clicked.connect(self.into_value)

    def into_value(self):
        list_value = []
        list_value.append(self.comboBox_unit.currentText())
        list_value.append(self.comboBox_subuint.currentText())
        list_value.append(self.lineEdit_kab.text())
        list_value.append(self.comboBox_name.currentText())
        list_value.append(self.lineEdit_count.text())
        list_value.append(datetime.today())
        moving_sheet.append(list_value)
        inv.save('../base_file/main.xlsx')



    # Изменения данных комбобокса Отделений
    def unit_selected(self, value):
        items_for_combo = []
        for name, count in inv[value].values:
            if count != 0 and type(count) == int:
                items_for_combo.append(name)
        self.comboBox_subuint.clear()
        self.comboBox_name.addItems(items_for_combo)
        self.comboBox_subuint.clear()
        self.comboBox_subuint.addItems(name_units[value])




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()






