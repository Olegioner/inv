# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inv.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 177)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 871, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 160, 80))
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 0, 160, 80))
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
        self.pushButton_clear = QtWidgets.QPushButton(self.frame)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 90, 158, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(350, 0, 91, 80))
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
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(460, 0, 321, 80))
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
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(800, 0, 71, 80))
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
        self.pushButton_into_values = QtWidgets.QPushButton(self.frame)
        self.pushButton_into_values.setGeometry(QtCore.QRect(644, 90, 141, 23))
        self.pushButton_into_values.setObjectName("pushButton_into_values")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 21))
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
        self.label_unit.setText(_translate("MainWindow", "Отделение"))
        self.label_subunit.setText(_translate("MainWindow", "Подразделение"))
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить"))
        self.label_kab.setText(_translate("MainWindow", "Кабинет"))
        self.label_name.setText(_translate("MainWindow", "Наименование"))
        self.label_count.setText(_translate("MainWindow", "Количество"))
        self.pushButton_into_values.setText(_translate("MainWindow", "Внести данные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
