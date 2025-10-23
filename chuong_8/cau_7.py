from tkinter import *


def chuyenAction():
    can = ["Giap", "At", "Binh", "Dinh", "Mau", "Ky", "Canh", "Tan", "Nham", "Quy"]
    chi = [
        "Ty",
        "Suu",
        "Dan",
        "Mao",
        "Thin",
        "Ty",
        "Ngo",
        "Mui",
        "Than",
        "Dau",
        "Tuat",
        "Hoi",
    ]

    can_index = (int(stringNhap.get()) + 6) % 10
    chi_index = (int(stringNhap.get()) + 8) % 12
    ketQua.config(text=can[can_index] + " " + chi[chi_index])


root = Tk()
root.title("tk")
root.minsize(width=500, height=500)
root.configure(padx=10, pady=10, bg="yellow", border=10)

stringNhap = StringVar()

Label(root, text="Nhap nam duong: ", bg="yellow").grid(row=0)
Entry(root, width=30, textvariable=stringNhap, borderwidth=2).grid(row=0, column=1)

Button(root, text="Chuyen", command=chuyenAction, bg="blue", fg="white").grid(
    row=1, column=1
)

Label(root, text="Nam am: ", bg="yellow").grid(row=2, column=0)
ketQua = Label(root, text="", bg="yellow")
ketQua.grid(row=2, column=1)

root.mainloop()
