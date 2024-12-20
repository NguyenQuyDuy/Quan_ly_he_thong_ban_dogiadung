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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import icon.qtframe_rc
import icon.icon_nav
import icon.iconframe_rc

class Ui_SignInWindow(object):
    def setupUi(self, SignInWindow):
        if not SignInWindow.objectName():
            SignInWindow.setObjectName(u"SignInWindow")
        SignInWindow.resize(763, 505)
        self.centralwidget = QWidget(SignInWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #FAC1C1;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(490, -10, 281, 541))
        self.frame.setStyleSheet(u"background-image: url(:/newPrefix/testui/images.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(80, 90, 371, 311))
        self.frame_2.setFocusPolicy(Qt.NoFocus)
        self.frame_2.setAcceptDrops(False)
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 20, 61, 31))
        font = QFont()
        font.setFamilies([u"Gill Sans MT Ext Condensed Bold"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 60, 31, 31))
        self.label_2.setStyleSheet(u"background-image: url(:/icon/ggicon.png);\n"
"border: 1px solid black;")
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setPixmap(QPixmap(u":/icon/ggicon.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 60, 31, 31))
        self.label_3.setStyleSheet(u"background-image: url(:/newPrefix/xicon.png);\n"
"border: 1px solid black")
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setPixmap(QPixmap(u":/newPrefix/xicon.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 100, 81, 20))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 130, 41, 16))
        self.txtEmail = QLineEdit(self.frame_2)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(70, 150, 241, 31))
        self.txtEmail.setStyleSheet(u"background-color: rgb(239, 250, 255);\n"
"border-radius: 10px;\n"
"padding:2px")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 190, 71, 16))
        self.txtpassword = QLineEdit(self.frame_2)
        self.txtpassword.setObjectName(u"txtpassword")
        self.txtpassword.setGeometry(QRect(70, 210, 241, 31))
        self.txtpassword.setStyleSheet(u"background-color: rgb(239, 250, 255);\n"
"border-radius: 10px;\n"
"padding:2px")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 260, 93, 28))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(246, 96, 96);\n"
"border-radius: 5px;\n"
"color: white")
        self.btSign_up = QPushButton(self.frame_2)
        self.btSign_up.setObjectName(u"btSign_up")
        self.btSign_up.setGeometry(QRect(200, 260, 93, 28))
        self.btSign_up.setCursor(QCursor(Qt.PointingHandCursor))
        self.btSign_up.setStyleSheet(u"background-color: rgb(246, 96, 96);\n"
"border-radius: 5px;\n"
"color: white")
        SignInWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignInWindow)

        QMetaObject.connectSlotsByName(SignInWindow)
    # setupUi

    def retranslateUi(self, SignInWindow):
        SignInWindow.setWindowTitle(QCoreApplication.translate("SignInWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SignInWindow", u"Sign In", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("SignInWindow", u"or sing in with", None))
        self.label_5.setText(QCoreApplication.translate("SignInWindow", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("SignInWindow", u"Passwords", None))
        self.pushButton.setText(QCoreApplication.translate("SignInWindow", u"Sign in", None))
        self.btSign_up.setText(QCoreApplication.translate("SignInWindow", u"Sign up", None))
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_SignInWindow()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())