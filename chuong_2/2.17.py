# Bài 17: Viết chương trình nhập số tự nhiên n và tính các giá trị sau:
# a) Tính tổng 1 + 2 + ... + 2n
# b) Tính tổng các số tự nhiên < n và là số lẻ
# c) Tính tổng các số tự nhiên < n và là số chẵn

n = int(input("Nhập số tự nhiên n: "))

# a) Tổng 1 + 2 + ... + 2n
tong_a = sum(range(1, 2*n +1))

# b) Tổng các số lẻ < n
tong_b = sum(i for i in range(1, n) if i % 2 != 0)

# c) Tổng các số chẵn < n
tong_c = sum(i for i in range(1, n) if i % 2 == 0)

print("a) Tổng 1 + 2 + ... + 2n =", tong_a)
print("b) Tổng các số lẻ <", n, "=", tong_b)
print("c) Tổng các số chẵn <", n, "=", tong_c)
