import math

def so_nguyen_to(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0: return False
  return True


while(True):
  n = int(input("Nhap vao so nguyen duong n: "))
  if n < 0: break
  if so_nguyen_to(n): print(f"{n} la so nguyen to")
  else: print(f"{n} khong phai la so nguyen to")
  check = int(input("Co nhap tiep de kiem tra khong (1/0): "))
  if check == 0: break
print("Ket thuc")