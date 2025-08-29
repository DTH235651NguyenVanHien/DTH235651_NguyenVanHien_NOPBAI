# Bài 16: Viết chương trình nhập 3 số tự nhiên day, month, year từ bàn phím.
# Kiểm tra xem bộ dữ liệu đã nhập có hợp lý hay không (ngày, tháng, năm hợp lệ).
# Quy tắc:
# - Tháng 1,3,5,7,8,10,12 có 31 ngày
# - Tháng 4,6,9,11 có 30 ngày
# - Tháng 2 có 28 hoặc 29 ngày (năm nhuận)
# - Năm nhuận khi: year % 400 == 0 hoặc (year % 4 == 0 và year % 100 != 0)

day = int(input("Nhap vao ngay:"))
month = int(input("Nhap vao thang:"))
year = int(input("Nhap vao nam:"))

check: bool = True

if year < 0:
    check = False
elif month < 1 or month > 12:
    check = False
else:
    if month in [1, 2, 3, 5, 7, 8, 10, 12]:
        if day < 0 or day > 31:
            check = False
    elif month in [4, 6, 9, 11]:
        if day < 0 or day > 30:
            check = False
    elif month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            if day < 0 or day > 29:
                check = False
        else:
            if day < 0 or day > 28:
                check = False

if check:
    print("Hop le")
else:
    print("Khong hop le")
