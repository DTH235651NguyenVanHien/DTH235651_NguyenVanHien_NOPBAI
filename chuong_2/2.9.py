# 9. Viết chương trình tỉnh:
# s - 1 + 2 +...+n
# Sl=1+3+...+ (2n - 1)
# S2= 2 + 4 +...+2n
# S3= I ^ 2 + 2 ^ 2 +...+n^ 2
# S4= 1/1 + 1/2 +...+1/n
# với n nguyên dương được nhập từ bàn phím.

n = int(input("Nhap so nguyen n: "))

print(f"Ket quan 1 + 2 + ... + {n} = {sum(i for i in range(1, n + 1))}")
