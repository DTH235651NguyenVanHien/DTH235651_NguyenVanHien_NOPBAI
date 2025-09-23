from random import randrange

n = int(input("Nhap so phan tu mang: "))
lst = [0]*n

for i in range(n):
  lst[i] = randrange(-100, 100)

print("Mang ngau nhien: ")
print(lst)

for i in range(n - 1):
  for j in range(i + 1, n):
    if lst[i] > lst[j]:
      lst[i], lst[j] = lst[j], lst[i]

print("Mang sau khi sap xep: ")
print(lst)