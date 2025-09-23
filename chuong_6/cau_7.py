n = int(input("Nhao vao so phan tu mang: "))

lst = [0]*n

for i in range(n):
  while(True):
    x = int(input())
    if x < lst[i - 1] and i > 0:
      print("Nhap lai")
      print(lst)
    else:
      lst[i] = x
      break

print(lst)
