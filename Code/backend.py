import sys
import inv_interfaces
from datetime import datetime, timedelta
from openpyxl import load_workbook
from PyQt5 import QtWidgets
from collections import Counter
import secret

inv = load_workbook(secret.file_way)

moving_sheet = inv['Движение']
plans_sheet = inv['Общий план']

name_units = {'Амбулатория': ['АО1', 'АО2', 'АО3', 'АО4', 'КДЛ', 'Платное отделение'],
              'Стационар' : ['Стационар'],
              'Дневной Стационар': ['ДС1', 'ДС2', 'ДС3', 'ДС4'],
              'Общий план': ['АО1', 'АО2', 'АО3', 'АО4', 'КДЛ',
                            'Платное отделение','Стационар','ДС1', 'ДС2', 'ДС3', 'ДС4']}



class ExampleApp(QtWidgets.QMainWindow, inv_interfaces.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации дизайна

    # Первый таб
        self.comboBox_unit.setPlaceholderText('Выберите отделение')
        self.comboBox_unit.addItems(list(name_units.keys()))
        self.comboBox_unit.currentTextChanged.connect(self.unit_selected)
        self.pushButton_into_values.clicked.connect(self.into_value)
    # Второй таб
        #Первичное заполнение combobox
        self.comboBox_unit_view.addItems(list(name_units.keys()))
        self.comboBox_sub_unit_view.addItems(name_units[self.comboBox_unit_view.currentText()])
        self.comboBox_unit_view.currentTextChanged.connect(self.unit_selected_for_sort)

        self.dateEdit_before.setDate(datetime.today() - timedelta(days=30))
        self.dateEdit_after.setDate(datetime.today() + timedelta(days=1))

        self.pushButton_view_info.clicked.connect(self.output_sort_info)



    # Ввод данных в exel
    def into_value(self):
        # Берем данные из необходимых полей
        unit = self.comboBox_unit.currentText()
        sub = self.comboBox_subuint.currentText()
        kab = self.lineEdit_kab.text()
        name_item = self.comboBox_name.currentText()
        count_item = self.lineEdit_count.text()
        list_value = [unit, sub, kab, name_item, count_item]
        list_value.append(datetime.today())


        #Ищем ячейку по значению и вычитаем из нее count_item
        for i in range(1, len(list(inv[unit].values))):
            cell_name = inv[unit][f'A{i}'].value
            cell_count = inv[unit][f'B{i}'].value
            if cell_name == name_item:
                if not count_item.isdigit():
                    self.label_info.setText('Количество может быть только целым числом')

                elif cell_count < int(count_item):
                    self.label_info.setText(f"Вы можете выдать только: {cell_count} шт.")

                else:
                    cell_count -= int(count_item)
                    inv[unit][f'B{i}'].value = cell_count

                    # Записываем данные на лист "Движение"
                    moving_sheet.append(list_value)

                    # Уменьшаем количество в общем плане
                    if unit != 'Общий план':
                        for j in range(1, len(list(plans_sheet.values))):
                            if plans_sheet[f'A{j}'].value == cell_name:
                                plans_sheet[f'B{j}'].value -= int(count_item)

                    # Сохраняем и выводим статус
                    inv.save(secret.file_way)
                    self.label_info.setText('Job is done!!!')

                    # Очищаем поля для дальнейшей работы
                    self.lineEdit_count.clear()
                    self.lineEdit_kab.clear()


    # Изменения данных комбобокса Отделений
    def unit_selected(self, value):
        items_for_combo = []
        for name, count in inv[value].values:
            if count != 0 and type(count) == int:
                items_for_combo.append(name)
        self.comboBox_name.clear()
        self.comboBox_name.addItems(items_for_combo)
        self.comboBox_subuint.clear()
        self.comboBox_subuint.addItems(name_units[value])


    # Изменения данных комбобокса Отделений(Сортировка)
    def unit_selected_for_sort(self, value):
        self.comboBox_sub_unit_view.clear()
        self.comboBox_sub_unit_view.addItems(name_units[value])


    # Вывод сортированных данных в TextEdit
    def output_sort_info(self):
        sorted_dict = Counter()
        self.textEdit_view_info.clear()
        # Получение данных для сортировки
        before = self.dateEdit_before.date()
        after = self.dateEdit_after.date()
        unit_view = self.comboBox_unit_view.currentText()
        sub_view = self.comboBox_sub_unit_view.currentText()
        for row in moving_sheet:
            unit, sub, kab, name, count, date = row
            if unit.value == unit_view:
                if sub.value == sub_view:
                    if date.value >= before and date.value < after:
                        sorted_dict[name.value] += int(count.value)
        if len(sorted_dict) == 0:
            self.textEdit_view_info.append('За указанный период данные не найдены')
        else:
            for key in sorted_dict.keys():
                self.textEdit_view_info.append(f'{sorted_dict[key]} -> {key}')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()





