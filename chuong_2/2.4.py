# 4. Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày. Ví dụ tháng 1. 3, 5, 7, 8, 10, 12 có 31 ngày. Tháng 4, 6, 9, 11 có 30 ngày. Nếu là tháng 2 thì yêu cầu nhập thêm năm. Năm nhuận thì tháng 2 có 29 ngày, không nhuẩn có 28 ngày.

thang = int(input("Nhap vao so thang: "))

if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("Thang", thang, "co 31 ngay")
elif thang in [4, 6, 9, 11]:
    print("Thang", thang, "co 30 ngay")
elif thang == 2:
    nam = int(input("Nhap vao nam: "))
    (
        print("Thang", thang, "co 29 ngay")
        if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
        else print("Thang", thang, "co 28 ngay")
    )
else:
    print("Thang khong hop le")
