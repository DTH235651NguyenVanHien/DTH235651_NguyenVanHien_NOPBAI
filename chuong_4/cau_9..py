import math

n = int(input("Nhap vao so can: "))

tong = 0

for _ in range(n):
  tong = math.sqrt(2 + tong)

print(tong)