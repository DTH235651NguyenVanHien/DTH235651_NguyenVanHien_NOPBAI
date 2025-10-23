from tkinter import *

def congAction():
  a = float(stringSoA.get())
  b = float(stringSoB.get())
  stringKQ.set(a + b)
  return

def truAction():
  a = float(stringSoA.get())
  b = float(stringSoB.get())
  stringKQ.set(a - b)
  return

def nhanAction():
  a = float(stringSoA.get())
  b = float(stringSoB.get())
  stringKQ.set(a * b)
  return

def chiaAction():
  a = float(stringSoA.get())
  b = float(stringSoB.get())
  if b == 0:
    stringKQ.set("Khong the chia cho 0")
    return
  stringKQ.set(a + b)
  return

root = Tk()
root.title("tk")
root.minsize(height=250, width=250)

stringSoA = StringVar()
stringSoB = StringVar()
stringKQ = StringVar()

Label(root, text="Cong tru nhan chia", justify=CENTER).grid(row=0, columnspan=3)

frameButton = Frame(root)
Button(frameButton, text="Cong", command=congAction).pack(side=TOP, fill=X)
Button(frameButton, text="Tru", command=truAction).pack(side=TOP, fill=X)
Button(frameButton, text="Nhan", command=nhanAction).pack(side=TOP, fill=X)
Button(frameButton, text="Chia", command=chiaAction).pack(side=TOP, fill=X)
frameButton.grid(row=1, column=0, rowspan=4)

Label(root, text="So a: ").grid(row=1, column=1)
Entry(root, width=30, textvariable=stringSoA).grid(row=1, column=2)

Label(root, text="So b: ").grid(row=2, column=1)
Entry(root, width=30, textvariable=stringSoB).grid(row=2, column=2)

Label(root, text="Ket qua: ").grid(row=3, column=1)
Entry(root, width=30, textvariable=stringKQ).grid(row=3, column=2)

Button(root, text="Thoat", command=root.quit).grid(row=4, column=2)

root.mainloop()