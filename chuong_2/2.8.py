# 8. Viết chương trình Python đọc số n (1 <n < 9) và in bảng cứu chương n.

n = int(input("Nhap vao so n: "))

if 2 <= n <= 9:
  for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
else:
  print("Khong hop le")