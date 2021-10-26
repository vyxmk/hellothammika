# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 387)
        MainWindow.setStyleSheet("background-color: rgb(252, 255, 237);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 10, 230, 60))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(25)
        self.output.setFont(font)
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output.setLineWidth(2)
        self.output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output.setObjectName("output")
        self.cbutt = QtWidgets.QPushButton(self.centralwidget)
        self.cbutt.setGeometry(QtCore.QRect(10, 80, 80, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.cbutt.setFont(font)
        self.cbutt.setObjectName("cbutt")
        self.butt7 = QtWidgets.QPushButton(self.centralwidget)
        self.butt7.setGeometry(QtCore.QRect(10, 135, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt7.setFont(font)
        self.butt7.setObjectName("butt7")
        self.butt4 = QtWidgets.QPushButton(self.centralwidget)
        self.butt4.setGeometry(QtCore.QRect(10, 190, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt4.setFont(font)
        self.butt4.setObjectName("butt4")
        self.butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.butt1.setGeometry(QtCore.QRect(10, 245, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt1.setFont(font)
        self.butt1.setObjectName("butt1")
        self.butt0 = QtWidgets.QPushButton(self.centralwidget)
        self.butt0.setGeometry(QtCore.QRect(10, 300, 111, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt0.setFont(font)
        self.butt0.setObjectName("butt0")
        self.butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.butt2.setGeometry(QtCore.QRect(70, 245, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt2.setFont(font)
        self.butt2.setObjectName("butt2")
        self.butt5 = QtWidgets.QPushButton(self.centralwidget)
        self.butt5.setGeometry(QtCore.QRect(70, 190, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt5.setFont(font)
        self.butt5.setObjectName("butt5")
        self.butt8 = QtWidgets.QPushButton(self.centralwidget)
        self.butt8.setGeometry(QtCore.QRect(70, 135, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt8.setFont(font)
        self.butt8.setObjectName("butt8")
        self.dotbutt = QtWidgets.QPushButton(self.centralwidget)
        self.dotbutt.setGeometry(QtCore.QRect(130, 300, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.dotbutt.setFont(font)
        self.dotbutt.setObjectName("dotbutt")
        self.butt3 = QtWidgets.QPushButton(self.centralwidget)
        self.butt3.setGeometry(QtCore.QRect(130, 245, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt3.setFont(font)
        self.butt3.setObjectName("butt3")
        self.butt6 = QtWidgets.QPushButton(self.centralwidget)
        self.butt6.setGeometry(QtCore.QRect(130, 190, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt6.setFont(font)
        self.butt6.setObjectName("butt6")
        self.butt9 = QtWidgets.QPushButton(self.centralwidget)
        self.butt9.setGeometry(QtCore.QRect(130, 135, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt9.setFont(font)
        self.butt9.setObjectName("butt9")
        self.equalbutt = QtWidgets.QPushButton(self.centralwidget)
        self.equalbutt.setGeometry(QtCore.QRect(190, 300, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.equalbutt.setFont(font)
        self.equalbutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.equalbutt.setObjectName("equalbutt")
        self.plusbutt = QtWidgets.QPushButton(self.centralwidget)
        self.plusbutt.setGeometry(QtCore.QRect(190, 245, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.plusbutt.setFont(font)
        self.plusbutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.plusbutt.setObjectName("plusbutt")
        self.minusbutt = QtWidgets.QPushButton(self.centralwidget)
        self.minusbutt.setGeometry(QtCore.QRect(190, 190, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.minusbutt.setFont(font)
        self.minusbutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.minusbutt.setObjectName("minusbutt")
        self.multibutt = QtWidgets.QPushButton(self.centralwidget)
        self.multibutt.setGeometry(QtCore.QRect(190, 135, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.multibutt.setFont(font)
        self.multibutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.multibutt.setObjectName("multibutt")
        self.dividebutt = QtWidgets.QPushButton(self.centralwidget)
        self.dividebutt.setGeometry(QtCore.QRect(190, 80, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.dividebutt.setFont(font)
        self.dividebutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.dividebutt.setObjectName("dividebutt")
        self.cebutt = QtWidgets.QPushButton(self.centralwidget)
        self.cebutt.setGeometry(QtCore.QRect(100, 80, 80, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.cebutt.setFont(font)
        self.cebutt.setObjectName("cebutt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple calculator"))
        self.output.setText(_translate("MainWindow", "0"))
        self.cbutt.setText(_translate("MainWindow", "C"))
        self.butt7.setText(_translate("MainWindow", "7"))
        self.butt4.setText(_translate("MainWindow", "4"))
        self.butt1.setText(_translate("MainWindow", "1"))
        self.butt0.setText(_translate("MainWindow", "0"))
        self.butt2.setText(_translate("MainWindow", "2"))
        self.butt5.setText(_translate("MainWindow", "5"))
        self.butt8.setText(_translate("MainWindow", "8"))
        self.dotbutt.setText(_translate("MainWindow", "."))
        self.butt3.setText(_translate("MainWindow", "3"))
        self.butt6.setText(_translate("MainWindow", "6"))
        self.butt9.setText(_translate("MainWindow", "9"))
        self.equalbutt.setText(_translate("MainWindow", "="))
        self.plusbutt.setText(_translate("MainWindow", "+"))
        self.minusbutt.setText(_translate("MainWindow", "-"))
        self.multibutt.setText(_translate("MainWindow", "x"))
        self.dividebutt.setText(_translate("MainWindow", "/"))
        self.cebutt.setText(_translate("MainWindow", "CE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
