def tong_uoc(n):
  return sum(i for i in range(1, int(n / 2 + 1)) if n % i == 0)

def hoan_hao(n):
  return tong_uoc(n) == n

def thinh_vuong(n):
  return tong_uoc(n) > n

n = int(input("Nhap vao so nguyen duong n: "))
print(f"{n} la so hoan hao") if hoan_hao(n) else print(f"{n} khong la so hoan hao")
print(f"{n} la so thinh vuong") if thinh_vuong(n) else print(f"{n} khong la so thinh vuong")