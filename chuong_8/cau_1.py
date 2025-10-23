from tkinter import *

def tiepAction():
  stringHSA.set("")
  stringHSB.set("")
  stringKQ.set("")

def giaiAction():
  a = float(stringHSA.get())
  b = float(stringHSB.get())
  if a == 0 and b == 0:
    stringKQ.set("Phuong trinh vo so nghiem")
  elif a == 0 and b != 0:
    stringKQ.set("Phuong trinh vo nghiem")
  else:
    stringKQ.set(f"Phuong trinh co nghiem x = {-b / a}")

root = Tk()

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

root.title("Phuong trinh bac 1")
root.minsize(height=130, width=250)
root.resizable(height=True, width=True)

Label(root, text="Phuong trinh bac 1", fg="red", font=("tohama",16), justify=CENTER).grid(row=0, columnspan=2)

Label(root, text="He so a: ").grid(row=1, column=0)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="He so b: ").grid(row=2, column=0)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

frameButton = Frame(root)
Button(frameButton, text="Giai", command=giaiAction).pack(side=RIGHT)
Button(frameButton, text="Tiep", command=tiepAction).pack(side=LEFT)
Button(frameButton, text="Thoat", command=root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=4)

Label(root, text="Ket qua: ").grid(row=4, column=0)
Entry(root, width=30, textvariable=stringKQ).grid(row=4, column=1)

root.mainloop()