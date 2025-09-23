import math

def nguyen_to(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0: return False
  return True

n = int(input("Nhao so phan tu mang: "))
lst = [0]*n

for i in range(n):
  lst[i] = int(input())

tong_le = 0
print("Cac so le: ")
for i in range(n):
  if lst[i] % 2 != 0:
    tong_le += lst[i]
    print(lst[i])
print("Tong cac so le: ", tong_le)

tong_chan = 0
print("Cac so chan: ")
for i in range(n):
  if lst[i] % 2 == 0:
    tong_chan += lst[i]
    print(lst[i])
print("Tong cac so chan: ", tong_chan)

print("Cac so nguyen to:")
for i in range(n):
  if nguyen_to(lst[i]):
    print(lst[i])

print("Cac so khong phai la so nguyen to:")
for i in range(n):
  if not nguyen_to(lst[i]):
    print(lst[i])
