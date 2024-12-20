import mysql.connector

def connectDatabase():
    mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='',
    database = 'bai1'
    )
    return mydb

# cursor = mydb.cursor()
# sql = "SELECT DISTINCT e.tennhanvien FROM bangnhanvien e JOIN kinangnhanvien s ON e.manhanvien = s.manhanvien;"
# cursor.execute(sql)
class bai1():

    def __init__(self):
        self.mydb = connectDatabase()
        self.cusor = self.mydb.cursor()
    
    def a(self):
        print("Nhân viên có ít nhất một kĩ năng là: ")
        sql = "SELECT DISTINCT e.tennhanvien FROM bangnhanvien e JOIN kinangnhanvien s ON e.manhanvien = s.manhanvien;"
        self.cusor.execute(sql)
        reSult = self.cusor.fetchall()
        for i in reSult:
            print(i)
    
    def b(self):
        print("Nhân viên có duy nhất một kĩ năng là: ")
        sql = "SELECT e.tennhanvien FROM bangnhanvien e JOIN kinangnhanvien s ON e.manhanvien = s.manhanvien GROUP BY e.manhanvien, e.tennhanvien HAVING COUNT(s.makynang) = 1;"
        self.cusor.execute(sql)
        reSult = self.cusor.fetchall()
        for i in reSult:
            print(i)
    def c(self):
        print("Nhân viên không có kĩ năng là: ")
        sql = "SELECT e.tennhanvien FROM bangnhanvien e LEFT JOIN kinangnhanvien s ON e.manhanvien = s.manhanvien WHERE s.manhanvien IS NULL;"
        self.cusor.execute(sql)
        reSult = self.cusor.fetchall()
        for i in reSult:
            print(i)
    def d(self):
        print("Nhân viên có nhiều kĩ năng là: ")
        sql = "SELECT e.tennhanvien FROM bangnhanvien e JOIN kinangnhanvien s ON e.manhanvien = s.manhanvien GROUP BY e.manhanvien, e.tennhanvien HAVING COUNT(s.makynang) >2;"
        self.cusor.execute(sql)
        reSult = self.cusor.fetchall()
        for i in reSult:
            print(i)
    
    def closeDatabase(self):
        self.cusor.close()
        self.mydb.close()


if __name__ == "__main__":
    app = bai1()

while True:
    action = input("Nhap y (a-d): (để xem kết quả), nhập bất kì để thoát: ")
    if action == "a":
        print("------------")
        app.a()
    elif action == "b":
        print("------------")
        app.b()
    elif action == "c":
        print("------------")
        app.c()
    elif action == "d":
        print("-----------")
        app.d()
    else:
        break

app.closeDatabase()


