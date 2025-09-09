chuoi = input("Nhap chuoi: ")

chuoi = chuoi.strip()
print(" ".join(tu.capitalize() for tu in chuoi.split()))