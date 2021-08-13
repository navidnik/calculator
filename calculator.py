# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calculator")
        MainWindow.resize(265, 459)
        MainWindow.setStyleSheet("background-color: #b7ced2\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.num_7 = QtWidgets.QPushButton(self.centralwidget)
        self.num_7.setGeometry(QtCore.QRect(7, 134, 61, 61))
        self.num_7.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_7.setObjectName("num_7")
        self.num_8 = QtWidgets.QPushButton(self.centralwidget)
        self.num_8.setGeometry(QtCore.QRect(70, 134, 61, 61))
        self.num_8.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_8.setObjectName("num_8")
        self.num_3 = QtWidgets.QPushButton(self.centralwidget)
        self.num_3.setGeometry(QtCore.QRect(133, 260, 61, 61))
        self.num_3.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_3.setObjectName("num_3")
        self.num_2 = QtWidgets.QPushButton(self.centralwidget)
        self.num_2.setGeometry(QtCore.QRect(70, 260, 61, 61))
        self.num_2.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_2.setObjectName("num_2")
        self.num_1 = QtWidgets.QPushButton(self.centralwidget)
        self.num_1.setGeometry(QtCore.QRect(7, 260, 61, 61))
        self.num_1.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_1.setObjectName("num_1")
        self.num_6 = QtWidgets.QPushButton(self.centralwidget)
        self.num_6.setGeometry(QtCore.QRect(133, 197, 61, 61))
        self.num_6.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_6.setObjectName("num_6")
        self.num_5 = QtWidgets.QPushButton(self.centralwidget)
        self.num_5.setGeometry(QtCore.QRect(70, 197, 61, 61))
        self.num_5.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_5.setObjectName("num_5")
        self.num_4 = QtWidgets.QPushButton(self.centralwidget)
        self.num_4.setGeometry(QtCore.QRect(7, 197, 61, 61))
        self.num_4.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_4.setObjectName("num_4")
        self.num_9 = QtWidgets.QPushButton(self.centralwidget)
        self.num_9.setGeometry(QtCore.QRect(133, 134, 61, 61))
        self.num_9.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.num_9.setObjectName("num_9")
        self.num_0 = QtWidgets.QPushButton(self.centralwidget)
        self.num_0.setGeometry(QtCore.QRect(7, 324, 124, 61))
        self.num_0.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250\n"
"\n"
"")
        self.num_0.setObjectName("num_0")
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(133, 324, 61, 61))
        self.dot.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.dot.setObjectName("dot")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(196, 324, 61, 61))
        self.equal.setStyleSheet("background-color: #B22222;\n"
"font-size: 25px;\n"
"")
        self.equal.setObjectName("equal")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(196, 260, 61, 61))
        self.plus.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(196, 197, 61, 61))
        self.minus.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.minus.setObjectName("minus")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(196, 134, 61, 61))
        self.multiply.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.multiply.setObjectName("multiply")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(196, 70, 61, 61))
        self.divide.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.divide.setObjectName("divide")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(7, 70, 124, 61))
        self.clear.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.clear.setObjectName("clear")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(133, 70, 61, 61))
        self.back.setStyleSheet("background-color: #528e86;\n"
"font-size: 25px;\n"
"color-hover: #636250")
        self.back.setObjectName("back")
        self.result = QtWidgets.QLineEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(7, 7, 251, 60))
        self.result.setStyleSheet("background-color: #dcdde2;")
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 400, 241, 31))
        self.label.setStyleSheet("font-size: 25px;\n"
"")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 21))
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
        self.num_7.setText(_translate("MainWindow", "7"))
        self.num_8.setText(_translate("MainWindow", "8"))
        self.num_3.setText(_translate("MainWindow", "3"))
        self.num_2.setText(_translate("MainWindow", "2"))
        self.num_1.setText(_translate("MainWindow", "1"))
        self.num_6.setText(_translate("MainWindow", "6"))
        self.num_5.setText(_translate("MainWindow", "5"))
        self.num_4.setText(_translate("MainWindow", "4"))
        self.num_9.setText(_translate("MainWindow", "9"))
        self.num_0.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.equal.setText(_translate("MainWindow", "="))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.back.setText(_translate("MainWindow", "<"))
        self.label.setText(_translate("MainWindow", "Design By: NavidNik"))


        # mycode for action

        self.num_0.clicked.connect(lambda: self.num_press('0'))
        self.num_1.clicked.connect(lambda: self.num_press('1'))
        self.num_2.clicked.connect(lambda: self.num_press('2'))
        self.num_3.clicked.connect(lambda: self.num_press('3'))
        self.num_4.clicked.connect(lambda: self.num_press('4'))
        self.num_5.clicked.connect(lambda: self.num_press('5'))
        self.num_6.clicked.connect(lambda: self.num_press('6'))
        self.num_7.clicked.connect(lambda: self.num_press('7'))
        self.num_8.clicked.connect(lambda: self.num_press('8'))
        self.num_9.clicked.connect(lambda: self.num_press('9'))
        self.dot.clicked.connect(lambda: self.num_press('.'))

        self.minus.clicked.connect(lambda: self.operator_press('-'))
        self.plus.clicked.connect(lambda: self.operator_press('+'))
        self.multiply.clicked.connect(lambda: self.operator_press('*'))
        self.divide.clicked.connect(lambda: self.operator_press('/'))

        self.back.clicked.connect(lambda: self.back_press())

        self.clear.clicked.connect(lambda: self.clear_press())

        self.equal.clicked.connect(lambda: self.equal_press())

    def num_press(self, number):
        expression = self.result.text()
        self.result.setText(expression + number)

    def operator_press(self, operator):
        expression = self.result.text()
        self.result.setText(expression + operator)

    def back_press(self):
        expression = self.result.text()
        if (len(expression)>0):
                expression = expression[:-1]
                self.result.setText(str(expression))
   
    def clear_press(self):
        self.result.setText('')

    def equal_press(self):
        try:
            expression = self.result.text()
            result = eval(expression)
            self.result.setText(str(result))
        except:
            self.result.setText("Invalid input!!! Please try again.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
