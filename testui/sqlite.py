# khởi tạo kết nối Database 
import sqlite3
con = sqlite3.connect('quanlysinhvien.db')
cur = con.cursor()
# Thêm sinh viên vào bảng dữ liệu
cur.execute("INSERT INTO sinhvien VALUES ('SV001','Nguyễn Văn Minh',0,'2000-01-10','Hà Nội')")
cur.execute("INSERT INTO sinhvien VALUES ('SV002','Phạm Thị Lan',1,'2000-06-02','Thái Bình')")
cur.execute("INSERT INTO sinhvien VALUES ('SV003','Lê Xuân Lan',1,'2001-05-02','Hà Nội')")
cur.execute("INSERT INTO sinhvien VALUES ('SV004','Nguyễn Như Quỳnh',1,'2001-01-04','Hải Phòng')")
# Cập nhật thay đổi vào Database
con.commit()
# Đóng kết nối Database
con.close()