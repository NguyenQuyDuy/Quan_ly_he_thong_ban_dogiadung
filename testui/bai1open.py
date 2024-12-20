import os


dirpath = os.path.dirname(__file__)
#-------------------------cau1--------------
file_path = os.path.join(dirpath, 'bai1file.txt')
file_path2 = os.path.join(dirpath, 'bai2.h5')
if not os.path.exists(file_path):
    print("Tep khong ton tai, tao tep moi")
    with open(file_path, 'w+') as file:
        file.write("Giang Xuan Cuong bai 1")
else:      
    with open(file_path, 'r') as file:
        content = file.read()
        print("Noi dung: ", content)
        
if not os.path.exists(file_path2):
    print("Tep khong ton tai, tao tep moi")
    with open(file_path2, 'w+') as file:
        file.write("Giang Xuan Cuong bai 2")
else:
    with open(file_path2, 'r') as file:
        content2 = file.read()
        print("Noi dung bai 2: ", content2)
#-------------------------------------------
#--------------cau2------------------