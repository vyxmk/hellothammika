from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(249, 388)
        MainWindow.setMaximumSize(QtCore.QSize(249, 388))
        MainWindow.setStyleSheet("background-color: rgb(252, 255, 237);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 19, 230, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        self.output.setFont(font)
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output.setLineWidth(2)
        self.output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output.setObjectName("output")

        self.cbutt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.c_it("C"))
        self.cbutt.setGeometry(QtCore.QRect(10, 80, 85, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.cbutt.setFont(font)
        self.cbutt.setObjectName("cbutt")

        self.butt7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7") )
        self.butt7.setGeometry(QtCore.QRect(10, 135, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt7.setFont(font)
        self.butt7.setObjectName("butt7")

        self.butt4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.butt4.setGeometry(QtCore.QRect(10, 190, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt4.setFont(font)
        self.butt4.setObjectName("butt4")

        self.butt1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.butt1.setGeometry(QtCore.QRect(10, 245, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt1.setFont(font)
        self.butt1.setObjectName("butt1")

        self.butt0 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.butt0.setGeometry(QtCore.QRect(10, 300, 111, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt0.setFont(font)
        self.butt0.setObjectName("butt0")

        self.butt2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.butt2.setGeometry(QtCore.QRect(70, 245, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt2.setFont(font)
        self.butt2.setObjectName("butt2")

        self.butt5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.butt5.setGeometry(QtCore.QRect(70, 190, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt5.setFont(font)
        self.butt5.setObjectName("butt5")

        self.butt8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.butt8.setGeometry(QtCore.QRect(70, 135, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt8.setFont(font)
        self.butt8.setObjectName("butt8")

        self.dotbutt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot_it())
        self.dotbutt.setGeometry(QtCore.QRect(130, 300, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.dotbutt.setFont(font)
        self.dotbutt.setObjectName("dotbutt")

        self.butt3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.butt3.setGeometry(QtCore.QRect(130, 245, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt3.setFont(font)
        self.butt3.setObjectName("butt3")

        self.butt6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.butt6.setGeometry(QtCore.QRect(130, 190, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt6.setFont(font)
        self.butt6.setObjectName("butt6")

        self.butt9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.butt9.setGeometry(QtCore.QRect(130, 135, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.butt9.setFont(font)
        self.butt9.setObjectName("butt9")

        self.equalbutt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.math_it())
        self.equalbutt.setGeometry(QtCore.QRect(190, 300, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.equalbutt.setFont(font)
        self.equalbutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.equalbutt.setObjectName("equalbutt")

        self.plusbutt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.plusbutt.setGeometry(QtCore.QRect(190, 245, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.plusbutt.setFont(font)
        self.plusbutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.plusbutt.setObjectName("plusbutt")

        self.minusbutt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.minusbutt.setGeometry(QtCore.QRect(190, 190, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.minusbutt.setFont(font)
        self.minusbutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.minusbutt.setObjectName("minusbutt")

        self.multibutt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("*"))
        self.multibutt.setGeometry(QtCore.QRect(190, 135, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.multibutt.setFont(font)
        self.multibutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.multibutt.setObjectName("multibutt")

        self.dividebutt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.dividebutt.setGeometry(QtCore.QRect(190, 80, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.dividebutt.setFont(font)
        self.dividebutt.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.dividebutt.setObjectName("dividebutt")

        self.delbutt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_it())
        self.delbutt.setGeometry(QtCore.QRect(100, 80, 80, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.delbutt.setFont(font)
        self.delbutt.setObjectName("delbutt")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 249, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   
    def math_it(self):
      
        screen = self.output.text()
        try:
            answer = eval(screen)
            if len(str(answer)) <= 15:
                if answer == 0.0:
                    self.output.setText("0")
                if answer >= 1 and answer % int(answer) == 0.0:
                    self.output.setText(str(int(answer)))
                else:
                    self.output.setText(str(answer))
            
            else:
                num = 15
                stranswer = str(answer)
                answer2 = answer
                if "." in stranswer:
                    while len(stranswer) > 15 and num > 0:
                        answer2 = round(answer2, num)
                        stranswer = str(answer2)
                        num -= 1
                    self.output.setText(stranswer)
                 
        except:
            self.output.setText("ERROR")
    
    def remove_it(self):
        screen = self.output.text()
        screen = screen[:-1]
        self.output.setText(screen)


    def dot_it(self):
        screen = self.output.text()
        if screen[-1] == ".":
            pass
        else:
            self.output.setText(f"{screen}.")

    def press_it(self, pressed):
        screen = self.output.text()
        screen = str(screen)

        if self.output.text() == "0":
            self.output.setText(pressed)
        else:
            self.output.setText(f'{self.output.text()}{pressed}')

    def c_it(self, pressed):
        if pressed == "C" :
            self.output.setText("0")


       
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
        self.delbutt.setText(_translate("MainWindow", "<<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
