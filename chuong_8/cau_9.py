from tkinter import *


def tinhAction():
    bmi = float(stringCan.get()) / float(stringCao.get()) ** 2
    stringBMI.set(bmi)

    if bmi < 18.5:
        StringTinhTrang.set("Gay")
    elif bmi <= 24.9:
        StringTinhTrang.set("Binh thuong")
    elif bmi <= 29.9:
        StringTinhTrang.set("Map")
    else:
        StringTinhTrang.set("Beo phi")


root = Tk()
root.minsize(height=250, width=250)
root.configure(bg="yellow")

stringCao = StringVar()
stringCan = StringVar()
stringBMI = StringVar()
StringTinhTrang = StringVar()
StringNguyCo = StringVar()

Label(root, text="Nhap chieu cao: ", bg="yellow").grid(row=0, column=0)
Entry(root, width=30, textvariable=stringCao, justify=CENTER, borderwidth=2, fg="red").grid(
    row=0, column=1
)

Label(root, text="Nhap can nang: ", bg="yellow").grid(row=1, column=0)
Entry(root, width=30, textvariable=stringCan, justify=CENTER, fg="red", borderwidth=2).grid(
    row=1, column=1
)

Button(root, text="TInh BMI", command=tinhAction, bg="blue", fg="white").grid(row=2, column=1)

Label(root, text="BMI cua ban: ", bg="yellow").grid(row=3, column=0)
Entry(root, width=30, textvariable=stringBMI, fg="red", justify=CENTER, borderwidth=2).grid(
    row=3, column=1
)

Label(root, text="Tinh trang cua ban: ", bg="yellow").grid(row=4, column=0)
Entry(root, width=30, textvariable=StringTinhTrang, fg="red", justify=CENTER, borderwidth=2).grid(
    row=4, column=1
)

Label(root, text="Nguyen co phat trien benh: ", bg="yellow").grid(row=5, column=0)
Entry(root, width=30, textvariable=StringNguyCo, fg="red", justify=CENTER, borderwidth=2).grid(
    row=5, column=1
)

Button(root, text="Thoat", command=root.quit, bg="blue", fg="white").grid(row=6, column=1)

root.mainloop()
