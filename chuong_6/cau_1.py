from random import randrange
import math

def nguyen_to(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

n = int(input("Nhap so phan tu list: "))
lst = [0]*n

for i in range(n):
  lst[i] = randrange(-100, 100)
print("List ngau nhien: ")
print(lst)

them = int(input("Nhap so can them: "))
lst.append(them)
print("List sau khi them: ")
print(lst)

dem = int(input("Nhap so can dem: "))
print(f"So lan xuat hien cua {dem} la: {lst.count(dem)}")

print(sum(so for so in lst if nguyen_to(so)))

lst.sort()
print("List sau khi sap xep: ")
print(lst)

lst.clear()
print("List sau khi xoa: ")
print(lst)