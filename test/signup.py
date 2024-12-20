import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox 
# tự thêm 2 thư viện cần thiết

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import bg.bgframe_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 626)
        MainWindow.setStyleSheet(u"background-color: rgb(250, 193, 193);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 40, 111, 41))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 100, 55, 16))
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtName = QLineEdit(self.centralwidget)
        self.txtName.setObjectName(u"txtName")
        self.txtName.setGeometry(QRect(70, 130, 391, 31))
        self.txtName.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:5px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 180, 71, 16))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtPassword = QLineEdit(self.centralwidget)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setGeometry(QRect(70, 210, 391, 31))
        self.txtPassword.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:5px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 260, 71, 16))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(70, 290, 391, 31))
        self.txtEmail.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:5px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 340, 121, 21))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtPhone = QLineEdit(self.centralwidget)
        self.txtPhone.setObjectName(u"txtPhone")
        self.txtPhone.setGeometry(QRect(70, 370, 391, 31))
        self.txtPhone.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:5px;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 430, 41, 21))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 430, 121, 21))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        
        
        values = ['Select role...','admin', 'sale', 'stocker']
        self.comboBox.addItems(values)
        
        self.btSignup = QPushButton(self.centralwidget)
        self.btSignup.setObjectName(u"btSignup")
        self.btSignup.setGeometry(QRect(150, 500, 93, 28))
        self.btSignup.setFont(font1)
        self.btSignup.setCursor(QCursor(Qt.PointingHandCursor))
        self.btSignup.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(246, 96, 96);\n"
"border-radius:5px")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(510, 0, 321, 631))
        self.frame.setStyleSheet(u"background-image: url(:/bg/images.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btSignin = QPushButton(self.centralwidget)
        self.btSignin.setObjectName(u"btSignin")
        self.btSignin.setGeometry(QRect(270, 500, 93, 28))
        self.btSignin.setFont(font1)
        self.btSignin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btSignin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(246, 96, 96);\n"
"border-radius:5px")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sign Up page", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.btSignup.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.btSignin.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())