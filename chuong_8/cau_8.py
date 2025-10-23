from tkinter import *

def chuyenAction():
  c = (float(stringNhap.get()) - 32) * 5 / 9
  lblKq.config(text=c)  

root = Tk()
root.title("tk")
root.minsize(height=250, width=250)
root.configure(padx=10, bg="yellow")

stringNhap = StringVar()

Label(root, text="Nhap do F: ", bg="yellow").grid()
Entry(root, width=40, textvariable=stringNhap, fg="red", justify=CENTER).grid(row=0, column=1)
Button(root, text="Chuyen", command=chuyenAction, bg="blue", fg="white").grid(row=1, column=1)

Label(root,  text="Do C", bg="yellow").grid(row=2)
lblKq =Label(root, text="", bg="yellow")
lblKq.grid(row=2, column=1)

root.mainloop()