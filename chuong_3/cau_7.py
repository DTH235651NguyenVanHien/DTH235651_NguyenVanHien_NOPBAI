ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))


def nam_nhuan(n):
    return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)


so_ngay_trong_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if nam_nhuan(nam):
    so_ngay_trong_thang[2] = 29

ngay += 1
if ngay > so_ngay_trong_thang[thang]:
    ngay = 1
    thang += 1
    if thang > 12:
        thang = 1
        nam += 1

print(f"Ngày kế tiếp là: {ngay}/{thang}/{nam}")
