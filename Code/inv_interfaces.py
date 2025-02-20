# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inv.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from openpyxl import load_workbook
inv = load_workbook('../base_file/main.xlsx')

name_sheet = inv['Наименования']
items_for_combo_name = []

for name, count in name_sheet.values:
    if count != 0 and type(count) == int:
        items_for_combo_name.append(name)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 140)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 761, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_kab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_kab.setObjectName("label_kab")
        self.gridLayout.addWidget(self.label_kab, 0, 3, 1, 1)
        self.label_count = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_count.setObjectName("label_count")
        self.gridLayout.addWidget(self.label_count, 0, 4, 1, 1)
        self.lineEdit_kab = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_kab.setObjectName("lineEdit_kab")
        self.gridLayout.addWidget(self.lineEdit_kab, 1, 3, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 2, 0, 1, 1)
        self.pushButton_into_values = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_into_values.setObjectName("pushButton_into_values")
        self.gridLayout.addWidget(self.pushButton_into_values, 2, 4, 1, 1)
        self.comboBox_unit = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_unit.setObjectName("comboBox_unit")
        self.gridLayout.addWidget(self.comboBox_unit, 1, 1, 1, 1)
        self.label_subunit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_subunit.setObjectName("label_subunit")
        self.gridLayout.addWidget(self.label_subunit, 0, 2, 1, 1)
        self.lineEdit_count = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_count.setObjectName("lineEdit_count")
        self.gridLayout.addWidget(self.lineEdit_count, 1, 4, 1, 1)
        self.comboBox_subuint = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_subuint.setObjectName("comboBox_subuint")
        self.gridLayout.addWidget(self.comboBox_subuint, 1, 2, 1, 1)
        self.comboBox_name = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_name.setObjectName("comboBox_name")
        self.comboBox_name.addItems(items_for_combo_name)
        self.gridLayout.addWidget(self.comboBox_name, 1, 0, 1, 1)
        self.label_unit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_unit.setObjectName("label_unit")
        self.gridLayout.addWidget(self.label_unit, 0, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_kab.setText(_translate("MainWindow", "Кабинет"))
        self.label_count.setText(_translate("MainWindow", "Количество"))
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_into_values.setText(_translate("MainWindow", "Внести данные"))
        self.label_subunit.setText(_translate("MainWindow", "Подразделение"))
        self.label_unit.setText(_translate("MainWindow", "Отделение"))
        self.label_name.setText(_translate("MainWindow", "Наименование"))



