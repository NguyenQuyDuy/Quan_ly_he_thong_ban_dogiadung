from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

app = CTk()
app.geometry("535x350")
app.title("Login system")
set_appearance_mode("info")

#-----------------------------
name_var = StringVar()
grade_var = StringVar()

#---------------
class add:
    def __init__(self):
        self.con = sqlite3.connect('lab1.db')
        self.cursor = self.con.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sinhvien (name TEXT, grade TEXT)''')
        self.con.commit()
        
    def addst(self):
        name = name_var.get()
        grade = grade_var.get()
        if name and grade:  # Kiểm tra nếu các trường không rỗng
            self.cursor.execute("INSERT INTO sinhvien VALUES (?,?)", (name, grade))
            self.con.commit()
            messagebox.showinfo("Success", "Add student success")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and grade")
    
    def clear(self):
        name_var.set("")
        grade_var.set("")
        
    def exit(self):
        self.cursor.close()
        self.con.close()
        app.quit()
        
add_ojb = add()

#----------------

frame = CTkFrame(
    master=app, 
    fg_color="#FAC1C1", 
    width=5335, height=350
    )
frame.place(x=0, y=0)

label = CTkLabel(
    master=frame,
    text="Lab 1",
    text_color="#ffffff",
    )
label.place(x=142, y=28)

label = CTkLabel(
    master=frame,
    text="Enter student's name",
    text_color="#ffffff",
    )
label.place(x=84, y=110)

entry = CTkEntry(
    master=frame,
    placeholder_text="Enter Student name..",
    width=210,
    height=26,
    corner_radius=6,
    border_color="white",
    textvariable=name_var)
entry.place(x=76, y=139)

label = CTkLabel(
    master=frame,
    text="Enter student's grade",
    text_color="#ffffff",
    )
label.place(x=84, y=170)

entry = CTkEntry(
    master=frame,
    placeholder_text="Enter student's grade..",
    width=210,
    height=26,
    corner_radius=6,
    border_color="white",
    textvariable=grade_var)
entry.place(x=76, y=190)

button = CTkButton(
    master=frame,
    text="Add",
    corner_radius=5,
    width=74,
    height=20,
    fg_color="#F66060",
    border_color="white",
    border_width=1,
    hover_color="#FFCC70",
    text_color="black",
    command=add_ojb.addst
)
button.place(x=92, y=239)

button_2 = CTkButton(
    master=frame,
    text="Clear",
    corner_radius=5,
    width=74,
    height=20,
    fg_color="#F66060",
    border_color="white",
    border_width=1,
    hover_color="#FFCC70",
    text_color="black",
    command=add_ojb.clear
)
button_2.place(x=184, y=239)

button_3 = CTkButton(
    master=frame,
    text="Exit",
    corner_radius=5,
    width=74,
    height=20,
    fg_color="#F66060",
    border_color="white",
    border_width=1,
    hover_color="#FFCC70",
    text_color="black",
    command=add_ojb.exit
)
button_3.place(x=276, y=239)

# Load and display image without showing any label text
img = Image.open("C:\\Users\\giang\\OneDrive\\Desktop\\testui\\images.jpg")
img_resize = img.resize((230, 450))
img_path = ImageTk.PhotoImage(img_resize)
canvas = CTkCanvas(
    master=frame,
    width=230,
    height=450,
    bg="#FAC1C1"  # Thay đổi màu nền của canvas để khớp với màu nền của frame
)
canvas.create_image(0, 0, anchor="nw", image=img_path)
canvas.place(x=450, y=0)

app.mainloop()
