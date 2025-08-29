# 6. Viết chương trình giải phương trình bậc 2: ax²+bx+c=0

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print(f"Phương trình cô nghiệm x = {-c / b}")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print(f"Phương trình cô nghiệm x = {-b / (2 * a)}")
    else:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        print(f"Phương trình cô hai nghiệm x1 = {x1} va x2 = {x2}")
