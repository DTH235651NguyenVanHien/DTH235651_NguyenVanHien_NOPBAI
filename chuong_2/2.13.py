# 13. Viết chương trình giải phương trình bậc 2 dạng: a * x ^ 2 + bx + c = 0 với các hệ số a, b, c được nhập từ bàn phím (a # 0).

while True:
    a = float(input("Nhap a: "))
    if a != 0:
        break
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

delta = b**2 - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print(f"Phuong trinh co nghiem x = {-b / (2 * a)}")
else:
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print(f"Phuong trinh co hai nghiem x1 = {x1} va x2 = {x2}")