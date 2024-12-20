import tkinter as tk
from PIL import Image, ImageQt
import sys
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame1(object):
    def setupUi(self, Frame1):
        Frame1.setObjectName("Frame1")
        Frame1.resize(844, 577)
        
        self.label = QtWidgets.QLabel(parent=Frame1)
        self.label.setGeometry(QtCore.QRect(380, 50, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(parent=Frame1)
        self.label_2.setGeometry(QtCore.QRect(160, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(parent=Frame1)
        self.label_3.setGeometry(QtCore.QRect(160, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.txtUsername = QtWidgets.QTextEdit(parent=Frame1)
        self.txtUsername.setGeometry(QtCore.QRect(250, 130, 391, 31))
        self.txtUsername.setObjectName("txtUsername")
        
        self.txtPassword = QtWidgets.QTextEdit(parent=Frame1)
        self.txtPassword.setGeometry(QtCore.QRect(250, 190, 391, 31))
        self.txtPassword.setObjectName("txtPassword")
        
        self.label_4 = QtWidgets.QLabel(parent=Frame1)
        self.label_4.setGeometry(QtCore.QRect(160, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(parent=Frame1)
        self.comboBox.setGeometry(QtCore.QRect(300, 250, 141, 22))
        self.comboBox.setObjectName("comboBox")
        valuess = ["Value 1", "Value 2", "Value 3"]
        self.comboBox.addItems(valuess)
        
        self.pushButton = QtWidgets.QPushButton(parent=Frame1)
        self.pushButton.setGeometry(QtCore.QRect(330, 330, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame1)
        QtCore.QMetaObject.connectSlotsByName(Frame1)
        
        self.addImage()

    def addImage(self):
        path = "user.png"
        
        img = Image.open(path)
        img = img.resize((25, 25), Image.Resampling.LANCZOS)
        
        imgQT = ImageQt.ImageQt(img)
        pixmap = QtGui.QPixmap.fromImage(imgQT)
        
        self.label.setPixmap(pixmap)
    def retranslateUi(self, Frame1):
        _translate = QtCore.QCoreApplication.translate
        Frame1.setWindowTitle(_translate("Frame1", "Dialog"))
        self.label.setText(_translate("Frame1", "Login"))
        self.label_2.setText(_translate("Frame1", "User name"))
        self.label_3.setText(_translate("Frame1", "Password"))
        self.label_4.setText(_translate("Frame1", "Gender"))
        self.pushButton.setText(_translate("Frame1", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame1 = QtWidgets.QDialog()
    ui = Ui_Frame1()
    ui.setupUi(Frame1)
    Frame1.show()
    sys.exit(app.exec())
