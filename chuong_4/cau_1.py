a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a <= 0 or b <= 0 or c <= 0 or (a+b) <= c or (a+c) <= b or (b+c) <= a:
  print("Tam giac khong hop le")
else:
  cv = a + b + c
  p = cv / 2
  dt = (p * (p - a) * (p - b) * (p - c)) ** 0.5
  print(f"Chu vi tam giac la: {cv}")
  print(f"Dien tich tam giac la: {dt}")