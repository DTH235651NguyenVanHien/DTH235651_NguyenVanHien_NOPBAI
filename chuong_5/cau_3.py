import math

chuoi = "5;7;8;-2;8;11;13;9;10"
list = map(int, chuoi.split(";"))


def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


so_chan = 0
so_am = 0
so_nguyen_to = 0
tong = 0
so_luong = 0

for i in list:
    if i % 2 == 0:
        so_chan += 1
    if i < 0:
        so_am += 1
    if nguyen_to(i):
        so_nguyen_to += 1
    tong += i
    so_luong += 1

print("So chan: ", so_chan)
print("So am: ", so_am)
print("So nguyen to: ", so_nguyen_to)
print("Trung binh: ", tong / so_luong)
