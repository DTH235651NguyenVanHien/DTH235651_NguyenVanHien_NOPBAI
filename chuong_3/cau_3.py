a = int(input("Nhap vao a: "))
b = int(input("Nhap vao b: "))
c = int(input("Nhap vao c: "))

if a == 0:
  if b == 0:
    if c == 0:
      print("Phuong trinh vo so nghiem")
    else:
      print("Phuong trinh vo nghiem")
  else: 
    print(f"Phuong trinh co nghiem x = {-c / b}")
else:
  delta = b**2 - 4*a*c
  if delta < 0:
    print("Phuong trinh vo nghiem")
  elif delta == 0:
    print(f"Phuong trinh co nghiem x = {-b / (2 * a)}")
  else:
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print(f"Phuong trinh co hai nghiem x1 = {x1} va x2 = {x2}")