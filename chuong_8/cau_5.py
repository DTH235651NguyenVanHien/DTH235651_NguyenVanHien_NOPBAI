from tkinter import *

def dangNhapAction():
  if stringNew.get() != stringAgain.get():
    print("Password khong khop")
    return
  print("Dang nhap thanh cong")
  return

root = Tk()
root.title("Enter new passsword")
root.minsize(height=500, width=500)

stringOld = StringVar()
stringNew = StringVar()
stringAgain = StringVar()

Label(root, text="Old password:").grid(row=0, column=0)
Entry(root, textvariable=stringOld, show="*", width=30).grid(row=0, column=1)

Label(root, text="New password").grid(row=1, column=0)
Entry(root, textvariable=stringNew, show="*", width=30).grid(row=1, column=1)

Label(root, text="Enter new password again").grid(row=2, column=0)
Entry(root, textvariable=stringAgain, show="*", width=30).grid(row=2, column=1)

frameButton = Frame(root)
Button(frameButton, text="OK", command=dangNhapAction).pack(side=LEFT)
Button(frameButton, text="Cancel", command=root.quit, bg="blue", fg="white").pack(side=LEFT)
frameButton.grid(row=3, columnspan=2)

root.mainloop()
