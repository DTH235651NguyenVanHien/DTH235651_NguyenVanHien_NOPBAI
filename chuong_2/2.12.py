# 12. Viết chương trình đổi số nguyên hệ thập phân ra số nhị phân.

n = int(input("Nhap vao so nguyen duong n: "))

print(bin(n)[2:])

def nhi_phan(n):
  if n == 0:
    return ""
  else: return nhi_phan(n // 2) + str(n % 2)

print(nhi_phan(n))