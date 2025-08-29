# 3. Viết chương trình Python tỉnh diện tích hình tròn với bán kinh được nhập từ bàn phím.

import math

ban_kinh = float(input("Nhap vao ban kinh: "))

dien_tich = math.pi * ban_kinh**2

print(f"Dien tich hinh tron co ban kinh {ban_kinh} la: {dien_tich:.2f}")
