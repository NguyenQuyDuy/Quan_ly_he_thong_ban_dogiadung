from customtkinter import *

# Tạo cửa sổ chính
app = CTk()
app.geometry("400x300")
app.title("Main Window")

# Hàm để mở cửa sổ con
def open_toplevel():
    top = CTkToplevel(app)
    top.geometry("300x200")
    top.title("Toplevel Window")

    label = CTkLabel(top, text="This is a Toplevel window")
    label.pack(pady=20)

    button = CTkButton(top, text="Close", command=top.destroy)
    button.pack(pady=10)

# Nút để mở cửa sổ con
button_open = CTkButton(app, text="Open Toplevel", command=open_toplevel)
button_open.pack(pady=20)

app.mainloop()
