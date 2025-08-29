# 11. Tỉnh dây số theo công thức. n nhập từ bàn phím.
# S(x,n)= x + (x ^ 2)/(2!) + (x ^ 3)/(3!) +...+ x^ 8 n!

import math

x = int(input("Nhap vao so nguyen duong x: "))
n = int(input("Nhap vao so nguyen duong n: "))

print(sum(x**i/math.factorial(i) for i in range(1, n + 1)))