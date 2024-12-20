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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import bg.bgTongquan
import iconbody.iconbody
import icon.icon_nav

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1290, 800)
        MainWindow.setMinimumSize(QSize(1290, 800))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 800))
        self.centralwidget.setMaximumSize(QSize(16777215, 850))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, 0, 1601, 80))
        self.frame.setStyleSheet(u"background-color: rgb(2, 154, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btTong_quan = QPushButton(self.frame)
        self.btTong_quan.setObjectName(u"btTong_quan")
        self.btTong_quan.setGeometry(QRect(10, 20, 121, 31))
        font = QFont()
        font.setBold(True)
        self.btTong_quan.setFont(font)
        self.btTong_quan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btTong_quan.setAcceptDrops(False)
        self.btTong_quan.setLayoutDirection(Qt.LeftToRight)
        self.btTong_quan.setAutoFillBackground(False)
        self.btTong_quan.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(217, 217, 217);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #FBE30B;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/tongquan35.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btTong_quan.setIcon(icon)
        self.btSan_pham = QPushButton(self.frame)
        self.btSan_pham.setObjectName(u"btSan_pham")
        self.btSan_pham.setGeometry(QRect(140, 20, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.btSan_pham.setFont(font1)
        self.btSan_pham.setCursor(QCursor(Qt.PointingHandCursor))
        self.btSan_pham.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(217, 217, 217);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #FBE30B;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/sanpham35.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btSan_pham.setIcon(icon1)
        self.btDon_hang = QPushButton(self.frame)
        self.btDon_hang.setObjectName(u"btDon_hang")
        self.btDon_hang.setGeometry(QRect(270, 20, 121, 31))
        self.btDon_hang.setFont(font1)
        self.btDon_hang.setCursor(QCursor(Qt.PointingHandCursor))
        self.btDon_hang.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(217, 217, 217);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #FBE30B;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/dh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btDon_hang.setIcon(icon2)
        self.btKhach_hang = QPushButton(self.frame)
        self.btKhach_hang.setObjectName(u"btKhach_hang")
        self.btKhach_hang.setGeometry(QRect(400, 20, 131, 31))
        self.btKhach_hang.setFont(font1)
        self.btKhach_hang.setCursor(QCursor(Qt.PointingHandCursor))
        self.btKhach_hang.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(217, 217, 217);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #FBE30B;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/khach35.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btKhach_hang.setIcon(icon3)
        self.btNhan_vien = QPushButton(self.frame)
        self.btNhan_vien.setObjectName(u"btNhan_vien")
        self.btNhan_vien.setGeometry(QRect(540, 20, 121, 31))
        self.btNhan_vien.setFont(font1)
        self.btNhan_vien.setCursor(QCursor(Qt.PointingHandCursor))
        self.btNhan_vien.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(217, 217, 217);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #FBE30B;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/nhanvien35.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btNhan_vien.setIcon(icon4)
        self.btTai_khoan = QPushButton(self.frame)
        self.btTai_khoan.setObjectName(u"btTai_khoan")
        self.btTai_khoan.setGeometry(QRect(1140, 20, 111, 31))
        self.btTai_khoan.setFont(font1)
        self.btTai_khoan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btTai_khoan.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(217, 217, 217);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #FBE30B;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/taikhoan35.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btTai_khoan.setIcon(icon5)
        self.btBan_hang = QPushButton(self.frame)
        self.btBan_hang.setObjectName(u"btBan_hang")
        self.btBan_hang.setGeometry(QRect(670, 20, 121, 31))
        self.btBan_hang.setFont(font1)
        self.btBan_hang.setCursor(QCursor(Qt.PointingHandCursor))
        self.btBan_hang.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(217, 217, 217);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #FBE30B;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/banhang35.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btBan_hang.setIcon(icon6)
        self.btQuan_li_tk = QPushButton(self.frame)
        self.btQuan_li_tk.setObjectName(u"btQuan_li_tk")
        self.btQuan_li_tk.setGeometry(QRect(810, 20, 181, 31))
        self.btQuan_li_tk.setFont(font1)
        self.btQuan_li_tk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btQuan_li_tk.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(217, 217, 217);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #FBE30B;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/qltaikhoan35.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btQuan_li_tk.setIcon(icon7)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, 79, 1291, 791))
        self.stackedWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.stackedWidget.setStyleSheet(u"background-color: #86d5e4;")
        self.pgTong_quan = QWidget()
        self.pgTong_quan.setObjectName(u"pgTong_quan")
        self.scrollArea = QScrollArea(self.pgTong_quan)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, 0, 941, 700))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(930, 700))
        self.scrollArea.setMaximumSize(QSize(950, 850))
        self.scrollArea.setStyleSheet(u"QScscrollArea{\n"
"	padding: 10px 0;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 922, 1603))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(900, 750))
        self.frame_3.setMaximumSize(QSize(900, 750))
        self.frame_3.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border-radius: 5px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 20, 161, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.Bd_doanh_thu = QTableWidget(self.frame_3)
        self.Bd_doanh_thu.setObjectName(u"Bd_doanh_thu")
        self.Bd_doanh_thu.setGeometry(QRect(10, 110, 881, 631))
        self.Bd_doanh_thu.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, -10, 900, 90))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(900, 90))
        self.frame_2.setMaximumSize(QSize(900, 90))
        self.frame_2.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border-radius: 5px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 111, 21))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        self.label.setFont(font3)
        self.txtTong_so_hoa_don = QLineEdit(self.frame_2)
        self.txtTong_so_hoa_don.setObjectName(u"txtTong_so_hoa_don")
        self.txtTong_so_hoa_don.setGeometry(QRect(170, 30, 171, 22))
        self.txtTong_so_hoa_don.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 30, 111, 21))
        self.label_2.setFont(font3)
        self.txtTong_doanh_thu = QLineEdit(self.frame_2)
        self.txtTong_doanh_thu.setObjectName(u"txtTong_doanh_thu")
        self.txtTong_doanh_thu.setGeometry(QRect(490, 20, 331, 51))
        font4 = QFont()
        font4.setPointSize(22)
        self.txtTong_doanh_thu.setFont(font4)
        self.txtTong_doanh_thu.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 80, 141, 16))
        self.label_5.setFont(font2)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(900, 550))
        self.frame_5.setMaximumSize(QSize(900, 550))
        self.frame_5.setStyleSheet(u"background-color: #D9D9D9;\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 161, 21))
        self.label_4.setFont(font2)
        self.bd_Sanpham_banchay = QTableWidget(self.frame_5)
        self.bd_Sanpham_banchay.setObjectName(u"bd_Sanpham_banchay")
        self.bd_Sanpham_banchay.setGeometry(QRect(10, 50, 881, 481))
        self.bd_Sanpham_banchay.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_5)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 250))

        self.verticalLayout_2.addWidget(self.widget)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_6 = QLabel(self.pgTong_quan)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(950, 0, 301, 61))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-image: url(:/tq/Banner-do-gia-dung.jpg);\n"
"border-radius:5px;\n"
"")
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setPixmap(QPixmap(u":/tq/Banner-do-gia-dung.jpg"))
        self.label_6.setScaledContents(True)
        self.widget_4 = QWidget(self.pgTong_quan)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(950, 70, 300, 570))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMinimumSize(QSize(250, 570))
        self.widget_4.setMaximumSize(QSize(300, 570))
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_3 = QScrollArea(self.widget_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QSize(250, 550))
        self.scrollArea_3.setMaximumSize(QSize(330, 550))
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(255, 241, 212);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 257, 579))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(230, 50))
        self.label_8.setMaximumSize(QSize(230, 50))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        self.label_8.setFont(font5)

        self.verticalLayout_6.addWidget(self.label_8)

        self.plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setMinimumSize(QSize(230, 500))
        self.plainTextEdit_2.setMaximumSize(QSize(230, 540))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;")

        self.verticalLayout_6.addWidget(self.plainTextEdit_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_5.addWidget(self.scrollArea_3)

        self.label_7 = QLabel(self.pgTong_quan)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(950, 650, 301, 61))
        self.label_7.setStyleSheet(u"background-image: url(:/tq/ftdgd.jpg);")
        self.label_7.setTextFormat(Qt.RichText)
        self.label_7.setPixmap(QPixmap(u":/tq/ftdgd.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.stackedWidget.addWidget(self.pgTong_quan)
        self.pgSan_pham = QWidget()
        self.pgSan_pham.setObjectName(u"pgSan_pham")
        self.widget_2 = QWidget(self.pgSan_pham)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1291, 721))
        self.frame_6 = QFrame(self.widget_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 2, 1291, 80))
        self.frame_6.setStyleSheet(u"background-color: rgb(131, 253, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 20, 121, 31))
        font6 = QFont()
        font6.setFamilies([u"Time new roman"])
        font6.setBold(True)
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"font-family: Time new roman;\n"
"font-weight: bold;")
        self.txtSearch = QLineEdit(self.frame_6)
        self.txtSearch.setObjectName(u"txtSearch")
        self.txtSearch.setGeometry(QRect(230, 19, 571, 31))
        self.txtSearch.setStyleSheet(u"QLineEdit{\n"
"border-radius: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"padding-left: 50px;\n"
"}\n"
"\n"
"\n"
"")
        self.btSearch = QPushButton(self.frame_6)
        self.btSearch.setObjectName(u"btSearch")
        self.btSearch.setGeometry(QRect(233, 21, 41, 28))
        self.btSearch.setCursor(QCursor(Qt.PointingHandCursor))
        self.btSearch.setStyleSheet(u"QPushButton{\n"
"	image: url(:/iconbd/icon/search35.png);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 252, 155);\n"
"}")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1080, 20, 93, 41))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"image: url(:/iconbd/icon/in35.png);")
        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 90, 911, 621))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.pgSan_pham)
        self.pgDonhang = QWidget()
        self.pgDonhang.setObjectName(u"pgDonhang")
        self.stackedWidget.addWidget(self.pgDonhang)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btTong_quan.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng quan", None))
        self.btSan_pham.setText(QCoreApplication.translate("MainWindow", u"S\u1ea3n ph\u1ea9m", None))
        self.btDon_hang.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n h\u00e0ng", None))
        self.btKhach_hang.setText(QCoreApplication.translate("MainWindow", u"Kh\u00e1ch h\u00e0ng", None))
        self.btNhan_vien.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e2n vi\u00ean", None))
        self.btTai_khoan.setText(QCoreApplication.translate("MainWindow", u"T\u00e0i kho\u1ea3n", None))
        self.btBan_hang.setText(QCoreApplication.translate("MainWindow", u"B\u00e1n h\u00e0ng", None))
        self.btQuan_li_tk.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00ed t\u00e0i kho\u1ea3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Doanh thu th\u00e1ng n\u00e0y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng s\u1ed1 h\u00f3a \u0111\u01a1n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng doanh thu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 doanh thu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"S\u1ea3n ph\u1ea9m b\u00e1n ch\u1ea1y", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng b\u00e1o \n"
" c\u00e1c ho\u1ea1t \u0111\u1ed9ng g\u1ea7n \u0111\u00e2y", None))
        self.label_7.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"S\u1ea3n ph\u1ea9m", None))
        self.btSearch.setText("")
        self.pushButton.setText("")
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btSan_pham.clicked.connect(self.sanpham)
        self.ui.btTong_quan.clicked.connect(self.tongquan)

    def sanpham(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pgSan_pham)  
    def tongquan(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pgTong_quan)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())