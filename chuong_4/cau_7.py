import math

xa = float(input("NHap vao toa do x cua A: "))
ya = float(input("Nhap vao toa do y cua A: "))
xb = float(input("Nhap vao toa do x cua B: "))
yb = float(input("Nhap vao toa do y cua B: "))

d = math.sqrt(math.pow(xa - xb, 2) + math.pow(ya - yb, 2))
print(f"Khoang cach giua hai diem la: {d}")