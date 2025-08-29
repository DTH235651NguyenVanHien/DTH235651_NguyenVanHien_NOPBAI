# Bài 20: Viết hàm f(m, n) với tham số là các số tự nhiên.
# Hàm trả lại số nguyên tố lớn nhất đồng thời là ước chung của m và n.
# Nếu không tồn tại thì trả lại 0.

import math


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def f(m, n):
    ucln = math.gcd(m, n)
    # Duyệt từ ucln xuống 2 để tìm số nguyên tố lớn nhất
    for i in range(ucln, 1, -1):
        if ucln % i == 0 and is_prime(i):
            return i
    return 0


# --- Ví dụ chạy ---
print("f(12, 18) =", f(12, 18))  # Ước chung nguyên tố lớn nhất là 3
print("f(8, 20) =", f(8, 20))  # Ước chung nguyên tố lớn nhất là 2
print("f(9, 25) =", f(9, 25))  # Không có, trả về 0
