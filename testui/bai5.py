import os


dirpath = os.path.dirname(__file__)
file_path = os.path.join(dirpath, 'setInfo.txt')

class bai5:
    def __init__(self, ten, tuoi, email, skype, diachi, noilmviec):
        self.ten = ten,
        self.tuoi = tuoi,
        self.email = email,
        self.skype = skype,
        self.diachi = diachi,
        self.noilmviec = noilmviec
    
    def nhap(self):
        self.ten = input("Nhap ten: ")
        self.tuoi = input("Nhap tuoi: ")
        self.email = input("Nhap email ca nhan: ")
        self.skype = input("Nhap skype: ")
        self.diachi = input("Nhap dia chi: ")
        self.noilamviec = input("Noi lam viec: ") 
            


