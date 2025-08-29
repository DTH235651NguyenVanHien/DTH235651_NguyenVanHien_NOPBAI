# Bài 18: Viết chương trình nhập số tự nhiên n và tính các giá trị sau:
# a) Số ước số nguyên tố khác nhau của n (tính cả n nếu n là số nguyên tố)
# b) Tổng các ước số thực sự của n (không tính n)
# c) Tính tổng 1^2 + 2^2 + 3^2 + ... + n^2

import math

n = int(input("Nhập số tự nhiên n: "))

# Hàm kiểm tra số nguyên tố
def is_prime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0: return False
  return True

# a) Số ước số nguyên tố khác nhau
so_ucsnt = len([i for i in range(1, n + 1) if is_prime(i) and n % i == 0])

# b) Tổng các ước số thực sự của n
tong_uoc = sum(i for i in range(1, n//2 + 1) if n % i == 0)

# c) Tổng 1^2 + 2^2 + ... + n^2
tong_binhphuong = sum(i**2 for i in range(n + 1))

print("a) Số ước số nguyên tố khác nhau của", n, "=", so_ucsnt)
print("b) Tổng các ước số thực sự của", n, "=", tong_uoc)
print("c) Tổng 1^2 + 2^2 + ... + n^2 =", tong_binhphuong)
