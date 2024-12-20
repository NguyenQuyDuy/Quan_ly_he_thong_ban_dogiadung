import tkinter as tk
from tkinter import ttk
from customtkinter import *
import sqlite3

app = tk.Tk()
app.geometry("535x350")
app.title("Student Information")

# Tạo Treeview
treeview = ttk.Treeview(app, columns=(1, 2), show="headings", height=5)
treeview.heading(1, text="Name")
treeview.heading(2, text="Grade")
treeview.pack()

def fetch_students():
    con = sqlite3.connect('lab1.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sinhvien")
    rows = cursor.fetchall()
    con.close()
    return rows

# Hiển thị dữ liệu trong Treeview
def display_students():
    students = fetch_students() 
    for student in students:
        treeview.insert("", "end", values=student)

display_students()

app.mainloop()
