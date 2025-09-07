nam = int(input("Nhap vao nam: "))

if nam % 4000 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    print("Nam nhuan")
else:
    print("Nam khong nhuan")
