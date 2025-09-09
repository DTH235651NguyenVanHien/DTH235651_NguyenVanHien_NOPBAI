import math

a = float(input("Nhap vao co so a: "))
x = float(input("Nhap vao he so x: "))

if x > 0 and a > 0 and a != 1:
  log_ax = math.log(x) / math.log(a)
  print(f"log_{a}({x}) = {log_ax}")
else:
  print("Khong hop le")