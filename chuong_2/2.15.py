# Bài 15: Viết chương trình nhập 3 số dương a, b, c trên một dòng (cách nhau bằng dau phay).
# Kiểm tra xem có thể tạo thành tam giác hay không.
# Điều kiện tam giác: a + b > c, a + c > b, b + c > a

a, b, c = map(float, input("Nhập 3 số dương a, b, c (cách nhau bằng khoảng trắng): ").split(","))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print("Có thể tạo thành một tam giác")
    else:
        print("Không thể tạo thành một tam giác")
else:
    print("Các cạnh phải là số dương")
