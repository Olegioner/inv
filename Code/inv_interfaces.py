# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inv.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QTextEdit



class Ui_MainWindow(object):

# Основное окно
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 871, 201))
        self.tabWidget.setObjectName("tabWidget")
# Вкладка ввода данных
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
    # Отделения
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_unit = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_unit.setObjectName("label_unit")
        self.verticalLayout.addWidget(self.label_unit)
        self.comboBox_unit = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_unit.setObjectName("comboBox_unit")
        self.verticalLayout.addWidget(self.comboBox_unit)

    # Подразделения
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 10, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_subunit = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_subunit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subunit.setObjectName("label_subunit")
        self.verticalLayout_2.addWidget(self.label_subunit)
        self.comboBox_subuint = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_subuint.setObjectName("comboBox_subuint")
        self.verticalLayout_2.addWidget(self.comboBox_subuint)
    # Кабинет
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(350, 10, 91, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_kab = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_kab.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kab.setObjectName("label_kab")
        self.verticalLayout_3.addWidget(self.label_kab)
        self.lineEdit_kab = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_kab.setObjectName("lineEdit_kab")
        self.verticalLayout_3.addWidget(self.lineEdit_kab)
    # Наименование
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(450, 10, 321, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_name = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_4.addWidget(self.label_name)
        self.comboBox_name = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_name.setObjectName("comboBox_name")
        self.verticalLayout_4.addWidget(self.comboBox_name)
    # Количество
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(780, 10, 71, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_count = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_count.setObjectName("label_count")
        self.verticalLayout_5.addWidget(self.label_count)
        self.lineEdit_count = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_count.setObjectName("lineEdit_count")
        self.verticalLayout_5.addWidget(self.lineEdit_count)
    # Очистка формы
        self.pushButton_clear = QtWidgets.QPushButton(self.tab)
        self.pushButton_clear.setGeometry(QtCore.QRect(10, 100, 158, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
    # Кнопка ввода данных
        self.pushButton_into_values = QtWidgets.QPushButton(self.tab)
        self.pushButton_into_values.setGeometry(QtCore.QRect(710, 100, 141, 23))
        self.pushButton_into_values.setObjectName("pushButton_into_values")
        self.tabWidget.addTab(self.tab, "")
# Вкладка вывод данных
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
    #Дата с:
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 160, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_start = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_start.setObjectName("label_start")
        self.verticalLayout_6.addWidget(self.label_start)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget_6)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_6.addWidget(self.dateEdit)
    #Дата по:
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(180, 10, 160, 41))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_finish = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_finish.setObjectName("label_finish")
        self.verticalLayout_7.addWidget(self.label_finish)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.verticalLayoutWidget_7)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout_7.addWidget(self.dateEdit_2)
    # Выбор отделения
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(350, 10, 160, 41))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_view_units = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_view_units.setObjectName("label_view_units")
        self.verticalLayout_8.addWidget(self.label_view_units)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_8.addWidget(self.comboBox)
    # Выбор Подразделения
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(520, 10, 160, 41))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_view_subunits = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_view_subunits.setObjectName("label_view_subunits")
        self.verticalLayout_9.addWidget(self.label_view_subunits)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_9)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_9.addWidget(self.comboBox_2)

    # Окно вывода
        self.textEdit_view_info = QTextEdit(self.tab_2)
        self.textEdit_view_info.setObjectName(u"textEdit_view_info")
        self.textEdit_view_info.setGeometry(QRect(10, 60, 851, 111))

    # Кнопка для вывода информации
        self.pushButton_view_info = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_view_info.setGeometry(QtCore.QRect(700, 20, 75, 23))
        self.pushButton_view_info.setObjectName("pushButton_view_info")

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_unit.setText(_translate("MainWindow", "Отделение"))
        self.label_subunit.setText(_translate("MainWindow", "Подразделение"))
        self.label_kab.setText(_translate("MainWindow", "Кабинет"))
        self.label_name.setText(_translate("MainWindow", "Наименование"))
        self.label_count.setText(_translate("MainWindow", "Количество"))
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_into_values.setText(_translate("MainWindow", "Внести данные"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Внесение данных"))
        self.label_start.setText(_translate("MainWindow", "Дата с:"))
        self.label_finish.setText(_translate("MainWindow", "Дата по:"))
        self.label_view_units.setText(_translate("MainWindow", "Отделение"))
        self.label_view_subunits.setText(_translate("MainWindow", "Подразделение"))
        self.pushButton_view_info.setText(_translate("MainWindow", "Показать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Данные за период"))
