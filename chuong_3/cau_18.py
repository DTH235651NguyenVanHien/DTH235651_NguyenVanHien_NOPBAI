# Nhập chiều cao
n = int(input("Nhập chiều cao n: "))

print("\nHình 1: Hình chữ nhật rỗng")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 2: Tam giác vuông cân (nằm góc dưới trái)")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nHình 3: Chữ L")
hinh3 = """
*
* *
*   *
* * * * * * *
        *   *
          * *
            *
"""

print(hinh3)
