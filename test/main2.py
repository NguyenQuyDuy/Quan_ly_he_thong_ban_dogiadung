from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QFileDialog
from PyQt6.uic import load_ui
import sys
import MySQLdb as mdb
import icon.qtframe_rc
import icon.iconframe_rc
import bg.bgTongquan
import icon.icon_nav
from wgTongquan import Ui_MainWindow as TQ
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import mplcursors

#Đăng nhập
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w, self).__init__()
        self.setWindowTitle('Login')
        self.setupUi()
        self.user_role = None #Them thuoc tinh de luu tru chuc vu nguoi dung
        self.Main_f = None 
    
    def setupUi(self):
        uic.loadUi('signin.ui', self)
        self.pushButton.clicked.connect(self.sign)
        self.btSign_up.clicked.connect(self.sign_up)
    def sign_up(self):
        widget.setFixedSize(770, 600)
        widget.setCurrentIndex(1)
    def sign(self):
        email = self.txtEmail.text()
        password =  self.txtpassword.text()  
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung') 
        query = db.cursor()
        query.execute("SELECT * FROM quan_li_tai_khoan WHERE email = %s AND mat_khau = %s", (email, password))
        kt=query.fetchone()
        if kt:
            self.user_role = kt[5]
            QMessageBox.information(self, "Signin out put", "Đăng nhập thành công")
            widget.setFixedSize(1290, 850)
            widget.setCurrentIndex(2)  
            self.Main_f.set_user_role(self.user_role)  
        elif(email == "" or password == ""):
            QMessageBox.information(self, "Sign out put", "Vui lòng điền email hoặc mật khẩu")
        else:
            QMessageBox.information(self, "Sign out put", "Sai tên tài khoản hoặc mật khẩu")

#Đăng kí   
class Reg_w(QMainWindow):
    def __init__(self):
        super(Reg_w, self).__init__()
        self.setWindowTitle('Sign_up')
        self.setupUi()
    def setupUi(self):
        uic.loadUi("signup.ui", self)
        self.btSignup.clicked.connect(self.signup)
        self.btSignin.clicked.connect(self.signin)
        
        self.setFixedSize(770, 600) #kích thước trang đăng kí
        values = ['Select role...', 'admin', 'sale', 'stocker']
        self.comboBox.addItems(values)
    
    def signin(self):
        widget.setFixedSize(763, 505)
        widget.setCurrentIndex(0)
    
    def signup(self):
        name = self.txtName.text()
        password = self.txtPassword.text()
        email = self.txtEmail.text()
        phoneNB = self.txtPhone.text()
        role = self.comboBox.currentText()
        
        if not name or not password or not email or not phoneNB or not role or role == 'Select role...':
            QMessageBox.information(self, "Sign Up", "Vui lòng điền đầy đủ thông tin và chọn vai trò hợp lệ")
            return 
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        
        query.execute("SELECT * FROM quan_li_tai_khoan WHERE email = %s", (email,))
        kt = query.fetchone()
        if kt:
            QMessageBox.information(self, "Sign Up", "Email đã tồn tại. Vui lòng sử dụng email khác.")
            db.close()
            return
        query.execute(
            "INSERT INTO quan_li_tai_khoan (ten, mat_khau, email, so_dien_thoai, chuc_vu) VALUES (%s, %s, %s, %s, %s)",
            (name, password, email, phoneNB, role))
        db.commit()  # Ghi lại thay đổi vào cơ sở dữ liệu
        QMessageBox.information(self, "Sign Up", "Đăng ký thành công")
        self.txtName.setText("")
        self.txtPassword.setText("")
        self.txtEmail.setText("")
        self.txtPhone.setText("")
        self.comboBox.setCurrentIndex(0)
    
        db.close()

#Tổng quan
class Main_w(QMainWindow):
    def __init__(self):
        super(Main_w, self).__init__()
        self.setWindowTitle("Tổng quan")
        self.user_role = None
        self.setupUi()
        
        
    def setupUi(self):
        uic.loadUi('wgTongquan.ui', self)
        
        #cac nut tren navbar
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        self.btTong_quan = self.findChild(QPushButton, "btTong_quan")
        self.btSan_pham = self.findChild(QPushButton, "btSan_pham")
        self.btDon_hang = self.findChild(QPushButton, "btDon_hang")
        self.btKhach_hang = self.findChild(QPushButton, "btKhach_hang")
        self.btNhan_vien = self.findChild(QPushButton, "btNhan_vien")
        self.btBan_hang = self.findChild(QPushButton, "btBan_hang")
        self.btQuan_li_tk = self.findChild(QPushButton, "btQuan_li_tk")
        self.btTai_khoan = self.findChild(QPushButton, "btTai_khoan")
        
        
        self.btTong_quan.clicked.connect(self.tongquanShow)
        self.btSan_pham.clicked.connect(self.sanphamShow)
        self.btDon_hang.clicked.connect(self.donhangShow)
        self.btKhach_hang.clicked.connect(self.khachhangShow)
        self.btNhan_vien.clicked.connect(self.nhanvienShow)
        self.btBan_hang.clicked.connect(self.banhangshow)
        self.btQuan_li_tk.clicked.connect(self.ql_taikhoan_show)
        self.btTai_khoan.clicked.connect(self.QL_Dangnhap)
                                                            #cac nut khac them sau
        
        # Tìm đối tượng QStackedWidget trong UI
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        
    def set_user_role(self, role):
        self.user_role = role
        self.setup_permission()
    def setup_permission(self):
        if self.user_role == 'sale':
            self.btSan_pham.setEnabled(False)
            self.btBan_hang.setEnabled(True)
            self.btTong_quan.setEnabled(False) # vo hieu hoa cac nut khong danh cho sale
            self.btDon_hang.setEnabled(True)
            self.btKhach_hang.setEnabled(True)
            self.btNhan_vien.setEnabled(False)
            self.btQuan_li_tk.setEnabled(False)
        elif self.user_role == 'admin':
            self.btSan_pham.setEnabled(True)
            self.btBan_hang.setEnabled(True)
            self.btTong_quan.setEnabled(True)
            self.btDon_hang.setEnabled(True)
            self.btKhach_hang.setEnabled(True)
            self.btNhan_vien.setEnabled(True)
            self.btQuan_li_tk.setEnabled(True)
        elif self.user_role == 'stocker':
            self.btSan_pham.setEnabled(True)
            self.btBan_hang.setEnabled(False)
            self.btTong_quan.setEnabled(False) # vo hieu hoa cac nut khong danh cho sale
            self.btDon_hang.setEnabled(False)
            self.btKhach_hang.setEnabled(False)
            self.btNhan_vien.setEnabled(False)
            self.btQuan_li_tk.setEnabled(False)
       
    def QL_Dangnhap(self):
        widget.setFixedSize(763, 505)
        widget.setCurrentIndex(0) 
    #-------------------------------- Tổng quan -----------------------------------
    def tongquanShow(self):
        self.stackedWidget.setCurrentIndex(0)
        self.pgTong_quan = self.stackedWidget.widget(0)
        self.load_ten_sp()
        self.bt_Tim_ma_sp = self.pgTong_quan.findChild(QPushButton, "bt_Tim_ma_sp")
        self.bt_Tim_ma_sp.clicked.connect(self.Tim_masp)
        
        txtTong_so_hoa_don = self.pgTong_quan.findChild(QLineEdit, "txtTong_so_hoa_don")
        txtTong_doanh_thu = self.pgTong_quan.findChild(QLineEdit, "txtTong_doanh_thu")
        self.Bd_doanh_thu = self.pgTong_quan.findChild(QTableWidget, "Bd_doanh_thu")
        self.bd_Sanpham_banchay  = self.pgTong_quan.findChild(QTableWidget, "bd_Sanpham_banchay")
        
        
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT COUNT(*) FROM don_hang"
        )
        result = query.fetchone()
        tong_so_don_hang = result[0]
        txtTong_so_hoa_don.setText(str(tong_so_don_hang))
        
        query.execute("SELECT SUM(tong_tien) FROM don_hang")
        result = query.fetchone()
        tong_tien = result[0] if result[0] is not None else 0 #lay tong tien tu kq
        txtTong_doanh_thu.setText(str(tong_tien))
        
        query.execute("SELECT ngay_dat_hang, ma_san_pham, SUM(tong_tien) FROM don_hang GROUP BY ngay_dat_hang, ma_san_pham")
        rows = query.fetchall()
        
        query.execute("SELECT ma_san_pham, SUM(tong_tien) as total FROM don_hang GROUP BY ma_san_pham ORDER BY total DESC LIMIT 10")
        top_products = query.fetchall()
        
        db.close()
        
        if rows:
            self.plot_bar_chart(rows)
        else: 
            self.Bd_doanh_thu.clearContents()
            self.Bd_doanh_thu.setRowCount(1)
            self.Bd_doanh_thu.setColumnCount(1)
            no_data_label = QLabel("Không có dữ liệu để hiển thị biểu đồ")
            self.Bd_doanh_thu.setCellWidget(0, 0, no_data_label)
            self.Bd_doanh_thu.setRowHeight(0, 620)
            self.Bd_doanh_thu.setColumnWidth(0, 800)
            
        if top_products :
            self.plot_top_products_chart(top_products)
        else:
            self.bd_Sanpham_banchay.clearContents()
            self.bd_Sanpham_banchay.setRowCount(1)
            self.bd_Sanpham_banchay.setColumnCount(1)
            no_data_label = QLabel("Không có dữ liệu để hiển thị biểu đồ")
            self.bd_Sanpham_banchay.setCellWidget(0, 0, no_data_label)
            self.bd_Sanpham_banchay.setRowHeight(0, 620)
            self.bd_Sanpham_banchay.setColumnWidth(0, 800)
            
    #Biểu đồ tổng doanh thu
    def plot_bar_chart(self, data):
        
        ngay_dat_hangs = sorted(set(row[0] for row in data))  # Danh sách các ngày đặt hàng duy nhất
        ma_san_phams = sorted(set(row[1] for row in data))    # Danh sách các mã sản phẩm duy nhất
    
        # Tạo một từ điển để lưu trữ tổng doanh thu của mỗi sản phẩm trong từng ngày
        revenue_data = {ngay_dat_hang: {ma_san_pham: 0 for ma_san_pham in ma_san_phams} for ngay_dat_hang in ngay_dat_hangs}
    
        # Điền dữ liệu doanh thu vào từ điển
        for row in data:
            ngay_dat_hang = row[0]
            ma_san_pham = row[1]
            tong_tien = row[2]
            revenue_data[ngay_dat_hang][ma_san_pham] += tong_tien
    
        # Vẽ biểu đồ
        fig, ax = plt.subplots()
        index = list(range(len(ngay_dat_hangs)))
        bar_width = 0.8 / len(ma_san_phams)  # Độ rộng của mỗi cột
         
        # Vẽ từng cột cho mỗi sản phẩm
        for i, ma_san_pham in enumerate(ma_san_phams):
            values = [revenue_data[ngay_dat_hang][ma_san_pham] for ngay_dat_hang in ngay_dat_hangs]
            ax.bar([idx + i * bar_width for idx in index], values, width=bar_width, label=f'Mã SP {ma_san_pham}')
    
        ax.set_xlabel('Ngày đặt hàng')
        ax.set_ylabel('Tổng tiền')
        ax.set_title('Biểu đồ tổng tiền theo ngày và mã sản phẩm')
        ax.set_xticks([idx + (len(ma_san_phams) - 1) * bar_width / 2 for idx in index])
        ax.set_xticklabels([str(ngay) for ngay in ngay_dat_hangs], rotation=45, ha='right')
        ax.legend()
    
    # Cập nhật biểu đồ vào bảng
        self.Bd_doanh_thu.clearContents()
        self.Bd_doanh_thu.setRowCount(1)
        self.Bd_doanh_thu.setColumnCount(1)
        canvas = FigureCanvas(fig)
        canvas_widget = QWidget()
        canvas_layout = QVBoxLayout()
        canvas_layout.addWidget(canvas)
        canvas_widget.setLayout(canvas_layout)
    
        self.Bd_doanh_thu.setCellWidget(0, 0, canvas_widget)
        self.Bd_doanh_thu.setRowHeight(0, 620)
        self.Bd_doanh_thu.setColumnWidth(0, 800)
    
    #Biểu đồ top sp bán chạy
    def plot_top_products_chart(self, top_products):
        ma_san_phams = [row[0] for row in top_products]
        total_revenues = [row[1] for row in top_products]
        
        # Vẽ biểu đồ
        fig, ax = plt.subplots()
        bars = ax.bar(ma_san_phams, total_revenues, color='blue')
        
        ax.set_xlabel('Mã Sản Phẩm')
        ax.set_ylabel('Tổng Doanh Thu')
        ax.set_title('Top 10 Sản Phẩm Bán Chạy Theo Doanh Thu')
        # Thêm chú thích khi di chuột
        cursor = mplcursors.cursor(bars)
        @cursor.connect("add")
        def on_add(sel):
            index = sel.index
            sel.annotation.set_text(f'Mã SP: {ma_san_phams[index]}')
        
        
        # Cập nhật biểu đồ vào bảng
        self.bd_Sanpham_banchay.clearContents()
        self.bd_Sanpham_banchay.setRowCount(1)
        self.bd_Sanpham_banchay.setColumnCount(1)
        canvas = FigureCanvas(fig)
        canvas_widget = QWidget()
        canvas_layout = QVBoxLayout()
        canvas_layout.addWidget(canvas)
        canvas_widget.setLayout(canvas_layout)
        
        self.bd_Sanpham_banchay.setCellWidget(0, 0, canvas_widget)
        self.bd_Sanpham_banchay.setRowHeight(0, 470)
        self.bd_Sanpham_banchay.setColumnWidth(0, 800)
        
        
        
        
    def load_ten_sp(self):
        tablewidget = self.pgTong_quan.findChild(QTableWidget, "tableWidget_8")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT ma_san_pham, ten_san_pham FROM san_pham"
        )
        rows = query.fetchall()
        tablewidget.setRowCount(0)
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(2)
        tablewidget.setHorizontalHeaderLabels(["Mã sản phẩm", "Tên sản phẩm"])
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        db.close()
         
    def Tim_masp(self):
        txtTim_ma_sp = self.pgTong_quan.findChild(QLineEdit, "txtTim_ma_sp").text()
        tablewidget = self.pgTong_quan.findChild(QTableWidget, "tableWidget_8")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT * FROM san_pham WHERE ma_san_pham = %s", (txtTim_ma_sp,)
        )
        rows = query.fetchall()
        db.commit()
        db.close()
        tablewidget.setRowCount(0)
        for row_index, row_data in enumerate(rows):
            tablewidget.insertRow(row_index)
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        
        
    
    #----------------------------------- Sản phẩm ------------------------------
    def sanphamShow(self):
        self.stackedWidget.setCurrentIndex(1)
        #thiet lap su kien cho nut them san pham
        self.pgSan_pham = self.stackedWidget.widget(1) #lay trang sp
        self.btThem = self.pgSan_pham.findChild(QPushButton, "btThem")
        self.btThem.clicked.connect(self.Themsp)
        self.btSua = self.pgSan_pham.findChild(QPushButton, "btSua")
        self.btSua.clicked.connect(self.Suasp)
        self.btSearch = self.pgSan_pham.findChild(QPushButton, "btSearch")
        self.btSearch.clicked.connect(self.Timkiem_sp)
        self.btXoa = self.pgSan_pham.findChild(QPushButton, "btXoa")
        self.btXoa.clicked.connect(self.xoaSP)
        self.btLam_moi = self.pgSan_pham.findChild(QPushButton, "btLam_moi")
        self.btLam_moi.clicked.connect(self.lammoi)
        self.load_san_pham()
        self.bt_In_sanpham = self.pgSan_pham.findChild(QPushButton, "bt_In_sanpham")
        self.bt_In_sanpham.clicked.connect(self.In_sanpham)
        
        self.tablewidget = self.pgSan_pham.findChild(QTableWidget, "tableWidget")
        self.tablewidget.itemClicked.connect(self.san_pham_info)
    #them san pham
    def Themsp(self):
        masanpham = self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").text()
        tensanpham = self.pgSan_pham.findChild(QLineEdit, "txtTen_san_pham").text()
        gia = self.pgSan_pham.findChild(QLineEdit, "txtGia").text()
        soluong = self.pgSan_pham.findChild(QLineEdit, "txtSo_luong").text()
        mota = self.pgSan_pham.findChild(QTextEdit, "txtMota").toPlainText()
        
        if (masanpham == "" or tensanpham =="" or gia =="" or soluong == "" or mota == ""):
            QMessageBox.information(self, "Cảnh báo", "Vui lòng nhập đầy đủ thông tin sản phẩm")
            return
        else:
            db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
            query = db.cursor()
            query.execute("SELECT * FROM san_pham WHERE ma_san_pham = %s", (masanpham,))
            kt = query.fetchone()
            if kt:
                QMessageBox.information(self, "Thông báo", "Mã sản phẩm đã tồn tại")
                self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").setText("")
                db.close()
                return
            query.execute("INSERT INTO san_pham (ma_san_pham, ten_san_pham, gia, so_luong_ton, mo_ta)" 
                          + "VALUES (%s, %s, %s, %s, %s)", (masanpham, tensanpham, gia,soluong, mota))
            
        db.commit()
        db.close()
        QMessageBox.information(self, "Thông báo", "Thêm sản phẩm thành công")
        self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtTen_san_pham").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtGia").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtSo_luong").setText("")
        self.pgSan_pham.findChild(QTextEdit, "txtMota").setText("")
        #cap nhat vao bang
        self.load_san_pham()
    
    #sửa sản phẩm
    def Suasp(self):
        masanpham = self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").text()
        tensanpham = self.pgSan_pham.findChild(QLineEdit, "txtTen_san_pham").text()
        gia = self.pgSan_pham.findChild(QLineEdit, "txtGia").text()
        soluong = self.pgSan_pham.findChild(QLineEdit, "txtSo_luong").text()
        mota = self.pgSan_pham.findChild(QTextEdit, "txtMota").toPlainText()
        
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "UPDATE san_pham SET ten_san_pham = %s, gia = %s, so_luong_ton = %s, mo_ta = %s WHERE ma_san_pham = %s",
                (tensanpham, gia, soluong, mota, masanpham)
            )
        db.commit()
        db.close()
        QMessageBox.information(self, "Thông báo", "Sửa sản phẩm thành công")
        self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtTen_san_pham").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtGia").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtSo_luong").setText("")
        self.pgSan_pham.findChild(QTextEdit, "txtMota").setText("")
        #cap nhat vao bang
        self.load_san_pham()
    
    #tìm kiếm sản phâmt
    def Timkiem_sp(self):
        
        txtSearch = self.pgSan_pham.findChild(QLineEdit, "txtSearch").text()
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT * FROM san_pham WHERE ten_san_pham LIKE %s", ("%"+txtSearch+"%",))
        rows = query.fetchall()
        db.commit()
        db.close()
        
        #cap nhat ket qua
        self.tablewidget.setRowCount(0)
        for row_index, row_data in enumerate(rows):
            self.tablewidget.insertRow(row_index)
            for column_index, data in enumerate(row_data):
                self.tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
    
    #Xóa
    def xoaSP(self):
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "DELETE FROM san_pham WHERE ma_san_pham = %s", (self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").text(),))
        db.commit()
        db.close()
        QMessageBox.information(self, "Thông báo", "Xóa thành công")
        self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtTen_san_pham").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtGia").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtSo_luong").setText("")
        self.pgSan_pham.findChild(QTextEdit, "txtMota").setText("")
        self.load_san_pham() 
        
    #hiển thị sản phẩm
    def load_san_pham(self):
        tablewidget = self.findChild(QTableWidget, "tableWidget")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute("SELECT * FROM san_pham")
        rows = query.fetchall()
        
        tablewidget.setRowCount(0) #xoa dl cu trong bang
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(5)
        tablewidget.setHorizontalHeaderLabels(["Mã sản phẩm", "Tên sản phẩm", "Giá", "Số Lượng", "Mô tả"])
        
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
                
        db.close()
    
    #hiển thị tt sản phẩm lên các ô tương ứng
    def san_pham_info(self, item):
        row = item.row()
        masanpham = self.tablewidget.item(row, 0).text()
        tensanpham = self.tablewidget.item(row, 1).text()
        gia = self.tablewidget.item(row, 2).text()
        soluong = self.tablewidget.item(row, 3).text()
        mota = self.tablewidget.item(row, 4).text()
        
        self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").setText(masanpham)
        self.pgSan_pham.findChild(QLineEdit, "txtTen_san_pham").setText(tensanpham)
        self.pgSan_pham.findChild(QLineEdit, "txtGia").setText(gia)
        self.pgSan_pham.findChild(QLineEdit, "txtSo_luong").setText(soluong)
        self.pgSan_pham.findChild(QTextEdit, "txtMota").setText(mota)
    
    #Lam moi
    def lammoi(self):
        self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtTen_san_pham").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtGia").setText("")
        self.pgSan_pham.findChild(QLineEdit, "txtSo_luong").setText("")
        self.pgSan_pham.findChild(QTextEdit, "txtMota").setText("")      
    
    def In_sanpham(self):
        self.bt_In_sanpham.setEnabled(False)
        txtMa_san_pham = self.pgSan_pham.findChild(QLineEdit, "txtMa_san_pham").text()
        txtTen_san_pham = self.pgSan_pham.findChild(QLineEdit, "txtTen_san_pham").text()
        txtGia = self.pgSan_pham.findChild(QLineEdit, "txtGia").text()
        txtSo_luong = self.pgSan_pham.findChild(QLineEdit, "txtSo_luong").text()
        txtMota = self.pgSan_pham.findChild(QTextEdit, "txtMota").toPlainText()
        
        content = f"==================== Thông tin sản phẩm ====================\n\n"
        content += f"Mã sản phẩm: {txtMa_san_pham}\n"
        content += f"Tên sản phẩm: {txtTen_san_pham}\n"
        content += f"Giá: {txtGia}\n"
        content += f"Số lượng: {txtSo_luong}\n"
        content += f"Mô tả: {txtMota}\n\n"
        content += f"==========================================================="
        
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('txt')
        file_path, _ = file_dialog.getSaveFileName(
            self, "Chọn nơi lưu trữ file", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            with open(file_path, 'w',encoding='utf-8') as file:
                file.write(content)
        self.bt_In_sanpham.setEnabled(True)
    # --------------------------------------- Đơn hàng-------------------
    def donhangShow(self):
        self.stackedWidget.setCurrentIndex(2)
        self.pgDonhang = self.stackedWidget.widget(2)
        self.btXoa_dh = self.pgDonhang.findChild(QPushButton, "btXoa_dh")
        self.btXoa_dh.clicked.connect(self.Xoa_dh)
        
        self.tablewidget = self.pgDonhang.findChild(QTableWidget, "tableWidget_2")
        self.tablewidget.clicked.connect(self.donhang_info)
        self.load_donhang()
        self.btSearch_donhang = self.pgDonhang.findChild(QPushButton, "btSearch_donhang")
        self.btSearch_donhang.clicked.connect(self.Tim_dh)
        
        self.btIn_donhang = self.pgDonhang.findChild(QPushButton, "btIn_donhang")
        self.btIn_donhang.clicked.connect(self.In_hoa_don)
        
    def In_hoa_don(self):
        self.btIn_donhang.setEnabled(False)
        txtMa_don_hang = self.pgDonhang.findChild(QLineEdit, "txtMa_don_hang").text()
        txtMa_san_pham_dh = self.pgDonhang.findChild(QLineEdit, "txtMa_san_pham_dh").text()
        txtSo_luong_sp = self.pgDonhang.findChild(QLineEdit, "txtSo_luong_sp").text()
        txtNgay_dat_hang = self.pgDonhang.findChild(QLineEdit, "txtNgay_dat_hang").text()
        txtTong_tien = self.pgDonhang.findChild(QLineEdit, "txtTong_tien").text()
        txtMa_khach_hang = self.pgDonhang.findChild(QLineEdit, "txtMa_khach_hang").text()
        
        content = f"=================== Hóa đơn bán hàng ====================\n\n"
        content += f"Mã đơn hàng: {txtMa_don_hang}\n"
        content += f"Mã sản phẩm: {txtMa_san_pham_dh}\n"
        content += f"Số lượng: {txtSo_luong_sp}\n"
        content += f"Ngày đặt hàng: {txtNgay_dat_hang}\n"
        content += f"Tổng tiền: {txtTong_tien}\n"
        content += f"Mã Khách hàng: {txtMa_khach_hang}\n"
        content += f"============================================================"
        
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('txt')
        file_path, _ = file_dialog.getSaveFileName(
            self, "Chọn nơi lưu trữ file", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            with open(file_path, 'w',encoding='utf-8') as file:
                file.write(content)
        self.btIn_donhang.setEnabled(True)
    
    def load_donhang(self):
        tablewidget = self.findChild(QTableWidget, "tableWidget_2")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute("SELECT * FROM don_hang")
        rows = query.fetchall()
        
        tablewidget.setRowCount(0)
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(6)
        tablewidget.setHorizontalHeaderLabels(["Mã đơn hàng", "Mã sản phẩm", "Số lượng", "Ngày đặt hàng", "Tổng tiền", "Mã khách hàng"])
        
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        db.close()
    
    def donhang_info(self, item):
        row = item.row()
        madonhang = self.tablewidget.item(row, 0).text()
        masanpham = self.tablewidget.item(row, 1).text()
        soluongsp = self.tablewidget.item(row, 2).text()
        ngaydathang = self.tablewidget.item(row, 3).text()
        tongtien = self.tablewidget.item(row, 4).text()
        makh = self.tablewidget.item(row, 5).text()
        
        self.pgDonhang.findChild(QLineEdit, "txtMa_don_hang").setText(madonhang)
        self.pgDonhang.findChild(QLineEdit, "txtMa_san_pham_dh").setText(masanpham)
        self.pgDonhang.findChild(QLineEdit, "txtSo_luong_sp").setText(soluongsp)
        self.pgDonhang.findChild(QLineEdit, "txtNgay_dat_hang").setText(ngaydathang)
        self.pgDonhang.findChild(QLineEdit, "txtTong_tien").setText(tongtien)
        self.pgDonhang.findChild(QLineEdit, "txtMa_khach_hang").setText(makh)
    
    def Xoa_dh(self):
        txtMa_don_hang = self.pgDonhang.findChild(QLineEdit, "txtMa_don_hang").text()
        
        confirm = QMessageBox.question(self, 'Xác nhận xóa', 
                                   f'Bạn có chắc chắn muốn xóa đơn hàng {txtMa_don_hang} không?',
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
            query = db.cursor()
            try:
                query.execute("DELETE FROM don_hang WHERE ma_don_hang = %s", (txtMa_don_hang,))
                db.commit()
                QMessageBox.information(self, "Thông báo", "Xóa đơn hàng thành công")
                # Xóa dữ liệu trong các QLineEdit sau khi xóa thành công
                self.pgDonhang.findChild(QLineEdit, "txtMa_don_hang").setText("")
                self.pgDonhang.findChild(QLineEdit, "txtMa_san_pham_dh").setText("")
                self.pgDonhang.findChild(QLineEdit, "txtSo_luong_sp").setText("")
                self.pgDonhang.findChild(QLineEdit, "txtNgay_dat_hang").setText("")
                self.pgDonhang.findChild(QLineEdit, "txtTong_tien").setText("")
                self.pgDonhang.findChild(QLineEdit, "txtMa_khach_hang").setText("")
                # Tải lại danh sách đơn hàng sau khi xóa
                self.load_donhang()
            except mdb.Error as e:
                db.rollback()
                QMessageBox.warning(self, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")
            finally:
                db.close()
        else:
            return
    
    def Tim_dh(self):
        txtSearch_donhang = self.pgDonhang.findChild(QLineEdit, "txtSearch_donhang").text()
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT * FROM don_hang WHERE ma_san_pham = %s", (txtSearch_donhang,)
        )
        rows = query.fetchall()
        db.commit()
        db.close()
        self.tablewidget.setRowCount(0)
        for row_index, row_data in enumerate(rows):
            self.tablewidget.insertRow(row_index)
            for column_index, data in enumerate(row_data):
                self.tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        
    #---------------------------------------Khách hàng -------------------
    def khachhangShow(self):
        self.stackedWidget.setCurrentIndex(3)
        self.pgKhach_hang = self.stackedWidget.widget(3)  #vị trí trang khách hàng
        self.btThem_kh = self.pgKhach_hang.findChild(QPushButton, "btThem_kh")
        self.btThem_kh.clicked.connect(self.themKH)
        self.btSua_kh = self.pgKhach_hang.findChild(QPushButton, "btSua_kh")
        self.btSua_kh.clicked.connect(self.SuaTT_khach_hang)
        self.btXoa_kh = self.pgKhach_hang.findChild(QPushButton, "btXoa_kh")
        self.btXoa_kh.clicked.connect(self.Xoa_kh)
        self.btSearch_kh = self.pgKhach_hang.findChild(QPushButton, "btSearch_kh")
        self.btSearch_kh.clicked.connect(self.Timkhiem_kh)
        
        self.bt_RF = self.pgKhach_hang.findChild(QPushButton, "bt_RF")
        self.bt_RF.clicked.connect(self.RF_kh)
        self.load_thongtin_khachang()
        
        self.tablewidget = self.pgKhach_hang.findChild(QTableWidget, "tableWidget_3")
        self.tablewidget.clicked.connect(self.khachhang_info)
    
    #Thêm khách hàng
    def themKH(self):
        txtMa_Khach_hang = self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").text()
        txtTen_khach_hang = self.pgKhach_hang.findChild(QLineEdit, "txtTen_khach_hang").text()
        txtSDT = self.pgKhach_hang.findChild(QLineEdit, "txtSDT").text()
        txtDiachi = self.pgKhach_hang.findChild(QLineEdit, "txtDiachi").text()
        txtEmail = self.pgKhach_hang.findChild(QLineEdit, "txtEmail").text()
        
        if (txtMa_Khach_hang == "" or txtTen_khach_hang =="" or txtSDT == "" or txtDiachi == "" or txtEmail == ""):
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng điền đầy đủ thông tin")  
            return
        else:
            db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
            query = db.cursor()
            query.execute("SELECT * FROM khach_hang WHERE ma_khach_hang = %s", (txtMa_Khach_hang,))
            kt = query.fetchone()
            if kt:
                QMessageBox.warning(self, "Cảnh báo", "Mã khách hàng đã tồn tại")
                self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").setText("")
                db.close()
                return
            query.execute(
                "INSERT INTO khach_hang (ma_khach_hang, ten_khach_hang, lien_he_khach_hang, dia_chi, email)"
                + "VALUES (%s, %s, %s, %s, %s)", (txtMa_Khach_hang, txtTen_khach_hang, txtSDT, txtDiachi, txtEmail))
        db.commit()
        db.close()
        QMessageBox.information(self, "Thông báo", "Thêm khách hàng thành công")
        self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtTen_khach_hang").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtSDT").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtDiachi").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtEmail").setText("")
        self.load_thongtin_khachang()
            
    #Sửa thông tin khách hàng
    def SuaTT_khach_hang(self):
        txtMa_Khach_hang = self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").text()
        txtTen_khach_hang = self.pgKhach_hang.findChild(QLineEdit, "txtTen_khach_hang").text()
        txtSDT = self.pgKhach_hang.findChild(QLineEdit, "txtSDT").text()
        txtDiachi = self.pgKhach_hang.findChild(QLineEdit, "txtDiachi").text()
        txtEmail = self.pgKhach_hang.findChild(QLineEdit, "txtEmail").text()
        
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "UPDATE khach_hang SET ten_khach_hang = %s, lien_he_khach_hang = %s, dia_chi = %s, email = %s WHERE ma_khach_hang = %s",
            (txtTen_khach_hang, txtSDT, txtDiachi, txtEmail, txtMa_Khach_hang)
        )
        db.commit()
        db.close()
        QMessageBox.information(self, "Thông báo", "Sửa khách hàng thành công")
        self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtTen_khach_hang").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtSDT").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtDiachi").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtEmail").setText("")
        self.load_thongtin_khachang()
    
   #Load thông tin khách hàng lên bảng
    def load_thongtin_khachang(self):
        tablewidget = self.findChild(QTableWidget, "tableWidget_3")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT * FROM khach_hang"
        )
        rows = query.fetchall()
        tablewidget.setRowCount(0) #Xoa dl cu trong bang
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(5)
        tablewidget.setHorizontalHeaderLabels(["Mã khách hàng", "Tên khách hàng", "Số điện thoại", "Địa chỉ", "Email"])
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        
        db.close()
        
    #hiển thị thông tin khách hàng lên các textBox
    def khachhang_info(self, item):
        row = item.row()
        makhachhang = self.tablewidget.item(row, 0).text()   
        tenkhachhang = self.tablewidget.item(row, 1).text()
        sdt = self.tablewidget.item(row, 2).text()
        diachi = self.tablewidget.item(row, 3).text()
        email = self.tablewidget.item(row, 4).text()
        
        self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").setText(makhachhang)
        self.pgKhach_hang.findChild(QLineEdit, "txtTen_khach_hang").setText(tenkhachhang)
        self.pgKhach_hang.findChild(QLineEdit, "txtSDT").setText(sdt)
        self.pgKhach_hang.findChild(QLineEdit, "txtDiachi").setText(diachi)
        self.pgKhach_hang.findChild(QLineEdit, "txtEmail").setText(email)  
    
    def RF_kh(self):
        self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtTen_khach_hang").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtSDT").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtDiachi").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtEmail").setText("")
     
    #Xóa khách hàng   
    def Xoa_kh(self):
        txtMa_khach_hang = self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").text()
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "DELETE FROM khach_hang WHERE ma_khach_hang = %s", (txtMa_khach_hang)
        )
        db.commit()
        db.close()
        QMessageBox.information(self, "Thông báo", "Xóa khách hàng thành công")
        self.pgKhach_hang.findChild(QLineEdit, "txtMa_Khach_hang").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtTen_khach_hang").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtSDT").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtDiachi").setText("")
        self.pgKhach_hang.findChild(QLineEdit, "txtEmail").setText("")
        self.load_thongtin_khachang()
    
    #Tìm kiếm khách hàng
    def Timkhiem_kh(self):
        txtSearch_khach_hang = self.pgKhach_hang.findChild(QLineEdit, "txtSearch_khach_hang").text()
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT * FROM khach_hang WHERE ten_khach_hang LIKE %s", ("%"+txtSearch_khach_hang+"%",))
        rows = query.fetchall()
        db.commit()
        db.close()
        
        self.tablewidget.setRowCount(0)
        for row_index, row_data in enumerate(rows):
            self.tablewidget.insertRow(row_index)
            for column_index, data in enumerate(row_data):
                self.tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        
    
    
    #-------------------------------- Nhân viên ------------------------
    def nhanvienShow(self):
        self.stackedWidget.setCurrentIndex(4)  
        self.pgNhan_vien = self.stackedWidget.widget(4)
        self.load_nhan_vien()
        self.btSearch_nv = self.pgNhan_vien.findChild(QPushButton, "btSearch_nv")
        self.btSearch_nv.clicked.connect(self.Search_nv)
        self.btXoa_nv = self.pgNhan_vien.findChild(QPushButton, "btXoa_nv")
        self.btXoa_nv.clicked.connect(self.Xoa_ttnv)
        
        self.btIn_nhanvien = self.pgNhan_vien.findChild(QPushButton, "btIn_nhanvien")
        self.btIn_nhanvien.clicked.connect(self.in_nhanvien)
        
        self.tablewidget = self.pgNhan_vien.findChild(QTableWidget, "tableWidget_4")
        self.tablewidget.itemClicked.connect(self.NV_info)
    
    def Xoa_ttnv(self):
        txtMaNV_Chamcong = self.pgNhan_vien.findChild(QLineEdit, "txtMaNV_Chamcong").text()
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "DELETE FROM cham_cong WHERE ma_nhan_vien = %s", (txtMaNV_Chamcong,)
        )
        db.commit()
        db.close()
        QMessageBox.information(self, "Thông báo", "Xóa nhân viên thành công")
        self.pgNhan_vien.findChild(QLineEdit, "txtMaNV_Chamcong").setText("")
        self.pgNhan_vien.findChild(QLineEdit, "txtTenNV_Chamcong").setText("")
        self.pgNhan_vien.findChild(QLineEdit, "txtTong_gio_lam").setText("")
        self.pgNhan_vien.findChild(QLineEdit, "txtTong_ca_lam").setText("")
        self.pgNhan_vien.findChild(QLineEdit, "txtTongLuong").setText("")
        self.load_nhan_vien()
    
    def  load_nhan_vien(self):
        tablewidget = self.findChild(QTableWidget, "tableWidget_4")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT * FROM cham_cong"
        )
        rows = query.fetchall()
        tablewidget.setRowCount(0)
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(7)
        tablewidget.setHorizontalHeaderLabels(["ID", "Mã nhân viên", "Tên nhân viên", "Ngày", "Giờ vào làm", "Giờ tan làm", "Lương"])
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        db.close()
        
    def Search_nv(self):
        txtSearch_nv = self.pgNhan_vien.findChild(QLineEdit,"txtSearch_nv").text()
        tablewidget =self.pgNhan_vien.findChild(QTableWidget, "tableWidget_4")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute("select * FROM cham_cong WHERE ten LIKE %s", ("%"+txtSearch_nv+"%",))
        rows = query.fetchall()
        db.commit()
        db.close()
        
        tablewidget.setRowCount(0)
        for row_index, row_data in enumerate(rows):
            tablewidget.insertRow(row_index)
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
                
    def NV_info(self, item):
        row = item.row()
        manhanvien = self.tablewidget.item(row, 1).text()
        tennhanvien = self.tablewidget.item(row, 2).text()
        
        self.pgNhan_vien.findChild(QLineEdit, "txtMaNV_Chamcong").setText(manhanvien)
        self.pgNhan_vien.findChild(QLineEdit, "txtTenNV_Chamcong").setText(tennhanvien)        
        
        txtTong_gio_lam = self.pgNhan_vien.findChild(QLineEdit, "txtTong_gio_lam")
        txtTong_ca_lam = self.pgNhan_vien.findChild(QLineEdit, "txtTong_ca_lam")
        txtTongLuong = self.pgNhan_vien.findChild(QLineEdit, "txtTongLuong")
        
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute("SELECT SUM(TIMESTAMPDIFF(SECOND, gio_vao, gio_ra)) FROM cham_cong WHERE ma_nhan_vien = %s", (manhanvien,))
        result = query.fetchone()
        tong_gio_lam_seconds = result[0] if result[0] is not None else 0
        tong_gio_lam_hours = tong_gio_lam_seconds / 3600
        txtTong_gio_lam.setText(f"{tong_gio_lam_hours:.2f}")
        
        query.execute(""" SELECT COUNT(*) FROM cham_cong WHERE ma_nhan_vien = %s""", (manhanvien,))
        result = query.fetchone()
        tong_ca_lam = result[0] if result[0] is not None else 0
        txtTong_ca_lam.setText(str(tong_ca_lam))
        
        query.execute("SELECT SUM(luong) FROM cham_cong WHERE ma_nhan_vien = %s", (manhanvien,))
        result = query.fetchone()
        tong_luong = result[0] if result[0] is not None else 0
        txtTongLuong.setText(str(tong_luong))
    
    def in_nhanvien(self):
        self.btIn_nhanvien.setEnabled(False)
        txtMaNV_Chamcong = self.pgNhan_vien.findChild(QLineEdit, "txtMaNV_Chamcong").text()
        txtTenNV_Chamcong = self.pgNhan_vien.findChild(QLineEdit, "txtTenNV_Chamcong").text()
        txtTong_gio_lam = self.pgNhan_vien.findChild(QLineEdit, "txtTong_gio_lam").text()
        txtTong_ca_lam = self.pgNhan_vien.findChild(QLineEdit, "txtTong_ca_lam").text()
        txtTongLuong = self.pgNhan_vien.findChild(QLineEdit, "txtTongLuong").text()
        
        content = f"================= Thông tin nhân viên==============\n\n"
        content += f"Mã nhân viên chấm công: {txtMaNV_Chamcong}\n"
        content += f"Tên Nhân Viên chấm công: {txtTenNV_Chamcong}\n"
        content += f"Tổng giờ làm: {txtTong_gio_lam}\n"
        content+= f"Tổng ca làm: {txtTong_ca_lam}\n"
        content+= f"Tổng Lương: {txtTongLuong}\n\n"
        content += f"======================================================="
        
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('txt')
        file_path, _ = file_dialog.getSaveFileName(
            self, "Chọn nơi lưu trữ", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        self.btIn_nhanvien.setEnabled(True)
        
    
    
    #-------------------------- Bán hàng -------------------------------
    def banhangshow(self):
        self.stackedWidget.setCurrentIndex(5)
        self.pgBan_hang = self.stackedWidget.widget(5) #vi tri trang ban hang
        self.load_san_pham_bh()
        self.load_tt_kh()
        self.btsearch_bh = self.pgBan_hang.findChild(QPushButton, "btsearch_bh")
        self.btsearch_bh.clicked.connect(self.Search_bh)
        self.btsearch_kh_bh = self.pgBan_hang.findChild(QPushButton, "btsearch_kh_bh")
        self.btsearch_kh_bh.clicked.connect(self.timkh_bh)
        self.btTinh_tien = self.pgBan_hang.findChild(QPushButton, "btTinh_tien")
        self.btTinh_tien.clicked.connect(self.Tinhtien)
        self.btThanh_toan = self.pgBan_hang.findChild(QPushButton, "btThanh_toan")
        self.btThanh_toan.clicked.connect(self.Thanhtoan)
        
        self.tablewidget = self.pgBan_hang.findChild(QTableWidget, "tableWidget_6")
        self.tablewidget.itemClicked.connect(self.banhang_info)
        
    
    def load_san_pham_bh(self):
        tablewidget = self.findChild(QTableWidget, "tableWidget_6")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "SELECT ma_san_pham, ten_san_pham, gia, mo_ta FROM san_pham;"
        )
        rows = query.fetchall()
        tablewidget.setRowCount(0)
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(4)
        tablewidget.setHorizontalHeaderLabels(["Mã sản phẩm", "Tên sản phẩm", "Giá", "Mô tả"])
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        db.close()
    def Search_bh(self):
        txtSearch_bh = self.pgBan_hang.findChild(QLineEdit, "txtSearch_bh").text()
        tablewidget = self.pgBan_hang.findChild(QTableWidget, "tableWidget_6")
        tablewidget.setRowCount(0)
        
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute("SELECT ma_san_pham, ten_san_pham, gia, mo_ta FROM san_pham WHERE ten_san_pham LIKE %s", ("%" + txtSearch_bh + "%",))
        rows = query.fetchall()
        db.close()
        
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(4)  # Số cột cần phù hợp với số cột truy vấn
        tablewidget.setHorizontalHeaderLabels(["Mã sản phẩm", "Tên sản phẩm", "Giá", "Mô tả"])
        
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                if column_index == 3:  # Cột "Mô tả"
                    tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
                else:  # Cột "Mã sản phẩm", "Tên sản phẩm", "Giá
                    tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
    
    def banhang_info(self, item):
        row = item.row()
        masanpham = self.tablewidget.item(row, 0).text()
        
        self.pgBan_hang.findChild(QLineEdit, "txtMa_sp_bh").setText(masanpham)
    
    def load_tt_kh(self):
        tablewidget = self.findChild(QTableWidget, "tableWidget_5")
        tablewidget.setRowCount(0)  # Xóa các hàng hiện có trong tablewidget
        tablewidget.setColumnCount(5)  # Đặt số cột cho tablewidget
        tablewidget.setHorizontalHeaderLabels(["Mã khách hàng", "Tên khách hàng", "Số điện thoại", "Địa chỉ", "Email"])
        
    def timkh_bh(self):
        txtsearch_mkh = self.pgBan_hang.findChild(QLineEdit, "txtsearch_mkh").text()
        tablewidget = self.pgBan_hang.findChild(QTableWidget, "tableWidget_5")
        tablewidget.setRowCount(0)
    
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute("SELECT * FROM khach_hang WHERE ten_khach_hang LIKE %s", ("%" + txtsearch_mkh + "%",))
        rows = query.fetchall()
        db.close()
    
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(5)
        tablewidget.setHorizontalHeaderLabels(["Mã khách hàng", "Tên khách hàng", "Số điện thoại", "Địa chỉ", "Email"])
    
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
    
    def Tinhtien(self):
        txtSo_luong_bh_widget = self.pgBan_hang.findChild(QLineEdit, "txtSo_luong_bh")
        txtGia_Tien_bh_widget = self.pgBan_hang.findChild(QLineEdit, "txtGia_Tien_bh")
        
        txtSo_luong_bh = txtSo_luong_bh_widget.text()
        txtGia_Tien_bh = txtGia_Tien_bh_widget.text()
       
        if txtSo_luong_bh.strip() and txtGia_Tien_bh.strip():  # Kiểm tra nếu txtGia_Tien_bh không rỗng hoặc chỉ chứa khoảng trắng
            try:
                so_luong = int(txtSo_luong_bh)
                gia = float(txtGia_Tien_bh)

                thanh_tien = so_luong * gia

                txtTong_tien_bh_widget = self.pgBan_hang.findChild(QLineEdit, "txtTong_tien_bh")
                txtTong_tien_bh_widget.setText(str(thanh_tien))
                
            except ValueError:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập số lượng và giá tiền hợp lệ")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập số lượng và giá tiền")
    
    def Thanhtoan(self):
        txtMa_sp_bh_widget = self.pgBan_hang.findChild(QLineEdit, "txtMa_sp_bh")
        txtSo_luong_bh_widget = self.pgBan_hang.findChild(QLineEdit, "txtSo_luong_bh")
        dateEdit_widget = self.pgBan_hang.findChild(QDateEdit, "dateEdit")
        txtTong_tien_bh_widget = self.pgBan_hang.findChild(QLineEdit, "txtTong_tien_bh")
        txtMa_kh_bh_widget = self.pgBan_hang.findChild(QLineEdit, "txtMa_kh_bh")
        
        txtMa_sp_bh = txtMa_sp_bh_widget.text()
        txtSo_luong_bh = txtSo_luong_bh_widget.text()
        dateEdit = dateEdit_widget.date()
        txtTong_tien_bh = txtTong_tien_bh_widget.text()
        txtMa_kh_bh = txtMa_kh_bh_widget.text()
        
        
        if not txtSo_luong_bh:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập số lượng")
            return
        so_luong_ton = int(txtSo_luong_bh)
        

        formatted_date = dateEdit.toString("yyyy-MM-dd")
        
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        try:
            query.execute("SELECT so_luong_ton FROM san_pham WHERE ma_san_pham = %s", (txtMa_sp_bh,))
            result = query.fetchone()
            if result is None:
                QMessageBox.warning(self, "Cảnh báo", "Sản phẩm không tồn tại")
                return
            current_so_luong = result[0]
            if current_so_luong < so_luong_ton:
                QMessageBox.warning(self, "Cảnh báo", "Số lượng sản phẩm không đủ")
                return
            db.begin()
            query.execute(
                "UPDATE san_pham SET so_luong_ton = so_luong_ton - %s WHERE ma_san_pham = %s", 
                (so_luong_ton, txtMa_sp_bh))
            
            query.execute(
                "INSERT INTO don_hang (ma_san_pham, so_luong, ngay_dat_hang, tong_tien, ma_khach_hang) VALUES (%s, %s, %s, %s, %s)",
                (txtMa_sp_bh, so_luong_ton, formatted_date, txtTong_tien_bh, txtMa_kh_bh))
            db.commit()
            QMessageBox.information(self, "Thành công", "Thanh toán thành công và thông tin hóa đơn đã được lưu")
            txtMa_sp_bh_widget.setText("")
            txtSo_luong_bh_widget.setText("")
            txtTong_tien_bh_widget.setText("")
            txtMa_kh_bh_widget.setText("")
        except mdb.Error as e:
            db.rollback()
            QMessageBox.warning(self, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")
        finally:
            db.close()
    #----------------------------- Quản lí tài khoản ----------------------------
    def ql_taikhoan_show(self):
        self.stackedWidget.setCurrentIndex(6)
        self.pgQuan_li_tk = self.stackedWidget.widget(6)
        self.load_tai_khoan()
        self.bt_Xoa_tk = self.pgQuan_li_tk.findChild(QPushButton, "bt_Xoa_tk")
        self.bt_Xoa_tk.clicked.connect(self.Xoa_ql_tk)
        self.bt_Sua_tk = self.pgQuan_li_tk.findChild(QPushButton, "bt_Sua_tk")
        self.bt_Sua_tk.clicked.connect(self.Sua_ql_tk)
        
        self.tablewidget = self.pgQuan_li_tk.findChild(QTableWidget, "tableWidget_7")
        self.tablewidget.clicked.connect(self.tai_khoan_info)
        
    def load_tai_khoan(self):
        tablewidget = self.pgQuan_li_tk.findChild(QTableWidget, "tableWidget_7")
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute("SELECT * FROM quan_li_tai_khoan")
        rows = query.fetchall()
        
        tablewidget.setRowCount(0)
        tablewidget.setRowCount(len(rows))
        tablewidget.setColumnCount(6)
        tablewidget.setHorizontalHeaderLabels(["ID", "Tên", "Mật khẩu", "Email", "Số điện thoại", "Chức vụ"])
        
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                tablewidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        db.close()
    
    def tai_khoan_info(self, item):
        row = item.row()
        id = self.tablewidget.item(row, 0).text() 
        ten = self.tablewidget.item(row, 1).text()
        matkhau = self.tablewidget.item(row, 2).text()
        email = self.tablewidget.item(row, 3).text()
        sodienthoai = self.tablewidget.item(row, 4).text()
        chucvu = self.tablewidget.item(row, 5).text()
        
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_ID_tk").setText(id)
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Ten_tk").setText(ten)
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Matkhau_tk").setText(matkhau)
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Email_tk").setText(email)
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Sodt_tk").setText(sodienthoai)
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Chucvu_tk").setText(chucvu)
    
    def Xoa_ql_tk(self):
        id = self.pgQuan_li_tk.findChild(QLineEdit, "txt_ID_tk").text()
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "DELETE FROM quan_li_tai_khoan WHERE id = %s", (id,)
        )
        db.commit()
        db.close()    
        QMessageBox.information(self, "Thông báo", "Xóa tài khoản thành công")
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_ID_tk").setText("")
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Ten_tk").setText("")
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Matkhau_tk").setText("")
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Email_tk").setText("")
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Sodt_tk").setText("")
        self.pgQuan_li_tk.findChild(QLineEdit, "txt_Chucvu_tk").setText("")
        self.load_tai_khoan()

    def Sua_ql_tk(self):
        
        txt_ID_tk = self.pgQuan_li_tk.findChild(QLineEdit, "txt_ID_tk").text()
        txt_Chucvu_tk = self.pgQuan_li_tk.findChild(QLineEdit, "txt_Chucvu_tk").text()
         
        db = mdb.connect('localhost', 'root', '', 'qlbandogiadung')
        query = db.cursor()
        query.execute(
            "UPDATE quan_li_tai_khoan SET chuc_vu = %s WHERE id = %s",
            (txt_Chucvu_tk, txt_ID_tk)
        )
        db.commit()
        db.close()
        QMessageBox.information(self, "Thông báo", "Thành công")
        self.load_tai_khoan()
         
        

        
    
    
if __name__ == "__main__":      
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_f = Login_w()
    reg_f =Reg_w()
    Main_f = Main_w()
    widget.addWidget(login_f)
    widget.addWidget(reg_f)
    widget.addWidget(Main_f)
    widget.setCurrentIndex(0)
    widget.setFixedHeight(500)
    widget.setFixedWidth(770)
    login_f.Main_f = Main_f
    widget.show()
    sys.exit(app.exec())