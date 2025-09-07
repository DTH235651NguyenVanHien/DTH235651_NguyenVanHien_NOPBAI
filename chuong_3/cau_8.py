a = int(input("Nhap vao a: "))
b = int(input("Nhap vao b: "))
toan_tu = input("Nhap vao toan tu: ")

if toan_tu == "+":
    print(a + b)
elif toan_tu == "-":
    print(a - b)
elif toan_tu == "*":
    print(a * b)
elif toan_tu == "/":
    print(a / b)
else:
    print("Toan tu khong hop le")
