import math

x = int(input("Nhap vao so nguyen duong x: "))
n = int(input("Nhap vao so nguyen duong n: "))

print(sum(x**i/math.factorial(i) for i in range(1, n + 1, 2)))