from tkinter import *


def nhapAction(so):
    stringKQ.set(stringKQ.get() + str(so))


def tinhAction():
    stringKQ.set(eval(stringKQ.get()))


root = Tk()
root.title("Calculator")
root.minsize(height=500, width=500)

stringKQ = StringVar()

Entry(root, textvariable=stringKQ).grid(row=0, column=0, columnspan=3)

Button(root, text="1", command=lambda: nhapAction("1")).grid(row=1, column=0)
Button(root, text="2", command=lambda: nhapAction("2")).grid(row=1, column=1)
Button(root, text="3", command=lambda: nhapAction("3")).grid(row=1, column=2)
Button(root, text="4", command=lambda: nhapAction("4")).grid(row=2, column=0)
Button(root, text="5", command=lambda: nhapAction("5")).grid(row=2, column=1)
Button(root, text="6", command=lambda: nhapAction("6")).grid(row=2, column=2)
Button(root, text="7", command=lambda: nhapAction("7")).grid(row=3, column=0)
Button(root, text="8", command=lambda: nhapAction("8")).grid(row=3, column=1)
Button(root, text="9", command=lambda: nhapAction("9")).grid(row=3, column=2)
Button(root, text="-", command=lambda: nhapAction("-")).grid(row=4, column=0)
Button(root, text="0", command=lambda: nhapAction("0")).grid(row=4, column=1)
Button(root, text=".", command=lambda: nhapAction(".")).grid(row=4, column=2)

frameButton = Frame(root)
Button(frameButton, text="+", command=lambda: nhapAction("+")).grid(row=0, column=0)
Button(frameButton, text="-", command=lambda: nhapAction("-")).grid(row=0, column=1)
Button(frameButton, text="*", command=lambda: nhapAction("*")).grid(row=0, column=2)
Button(frameButton, text="/", command=lambda: nhapAction("/")).grid(row=0, column=3)
Button(frameButton, text="=", command=tinhAction).grid(row=0, column=4)
frameButton.grid(row=5, columnspan=3)

Button(root, text="Clr", command=lambda: stringKQ.set("")).grid(row=6, columnspan=3)
Button(root, text="Del", command=lambda: stringKQ.set(stringKQ.get()[:-1])).grid(
    row=7, columnspan=3
)


root.mainloop()
