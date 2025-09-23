from random import randrange

lst = []
n = int(input("Nhap so phan tu mang: "))

for i in range(n):
    lst.append(randrange(0, 100))

print("Mang ngau nhien: ")
print(lst)

them = int(input("Nhap so can them: "))
lst.append(them)
print("Mang sau khi them: ")
print(lst)

xoa = int(input("Nhap so can xoa: "))
if lst.count(xoa) > 0:
    lst.remove(xoa)
    print("Mang sau khi xoa: ")
    print(lst)
else :
    print("Khong tim thay so can xoa")

def doi_xung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

if doi_xung(lst):
    print("Mang doi xung")
else:
    print("Mang khong doi xung")