from tkinter import *
import math


def giaiAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    c = float(stringHSC.get())

    if a == 0:
        if b == 0:
            if c == 0:
                stringKQ.set("Phuong trinh vo so nghiem")
            else:
                stringKQ.set("Phuong trinh vo nghiem")
        else:
            stringKQ.set(f"Phuong tirnh co nghiem la: x= ", (-c / b))
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            stringKQ.set("Phuong trinh vo nghiem")
        elif delta == 0:
            stringKQ.set(f"Phuong trinh co nghiem kep x1 = x2 =", (-b / 2 * a))
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            stringKQ.set(f"Phuong trinh co hai nghiem x1 = {x1} x2 = {x2}")
    return


def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")


root = Tk()
root.title("Phuong trinh bac 2")
root.minsize(height=150, width=250)

stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

Label(root, text="Phuong trinh bac 2", fg="red", font=("tohama", 16)).grid(
    row=0, column=0, columnspan=2
)
Label(root, text="He so a: ").grid(row=1, column=0)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="He so b: ").grid(row=2, column=0)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

Label(root, text="He so c: ").grid(row=3, column=0)
Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1)

frameButton = Frame(root)
Button(frameButton, text="Giai", command=giaiAction).pack(side=RIGHT)
Button(frameButton, text="Tiep", command=tiepAction).pack(side=LEFT)
Button(frameButton, text="Thoat", command=root.quit).pack(side=LEFT)
frameButton.grid(row=4, columnspan=2)

Label(root, text="Ket qua: ").grid(row=5, column=0)
Entry(root, width=30, textvariable=stringKQ).grid(row=5, column=1)

root.mainloop()
