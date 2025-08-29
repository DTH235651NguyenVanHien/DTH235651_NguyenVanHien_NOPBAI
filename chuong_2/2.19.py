# Bài 19: Viết các thủ tục thực hiện các công việc sau:

import math

# Tổng 1 + 2 + ... + n
def tinh_tong(n):
    return sum(i for i in range(1, n + 1))


n = int(input("Nhap vao n: "))
print(tinh_tong(n))


# b) Tham số là 2 số m, n, kiểm tra nguyên tố cùng nhau (ước chung lớn nhất = 1)
def kiem_tra_nguyen_to_cung_nhau(m, n):
    if math.gcd(m, n) == 1:
        return print("Nguyen to cung nhau")
    return print("Khong nguyen to cung nhau")


m = int(input("Nhap vao m: "))
n = int(input("Nhap vao n: "))

kiem_tra_nguyen_to_cung_nhau(m, n)


# c) Tham số là số giây s, chuyển sang giờ, phút, giây
def doi_giay(s):
    gio = s // 3600
    phut = (s % 3600) // 60
    giay = s % 60
    print(f"{s} giây = {gio} giờ {phut} phút {giay} giây")
doi_giay(int(input("Nhap vao giay: ")))

# d) Trị tuyệt đối |a - b|
def tri_tuyet_doi(a, b):
    return abs(a - b)

a = int(input("Nhap vao a: "))
b = int(input("Nhap vao b: "))
print(tri_tuyet_doi(a, b))
