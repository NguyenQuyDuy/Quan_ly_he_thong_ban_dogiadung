# khởi tạo kết nối Database 
import sqlite3
con = sqlite3.connect('quanlysinhvien.db')
cur = con.cursor()
# Lấy ra danh sách các sinh viên có họ "Nguyễn"
dataset = cur.execute("SELECT * FROM sinhvien WHERE HoVaTen LIKE 'Nguyễn%'")
for row in dataset:
    print(row)
# Đóng kết nối Database
con.close()

# khởi tạo kết nối Database 
# import sqlite3
# con = sqlite3.connect('quanlysinhvien.db')
# cur = con.cursor()
# # Sửa họ và tên của sinh viên có mã là 'SV001'
# cur.execute("UPDATE sinhvien SET HoVaTen='Nguyễn Văn An' WHERE MaSinhVien='SV001'")
# # Cập nhật thay đổi vào Database
# con.commit()
# # Đóng kết nối Database
# con.close()
