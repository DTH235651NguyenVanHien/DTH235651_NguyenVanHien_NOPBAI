chuoi = input("Nhap chuoi: ")

hoa = 0
thuong = 0
so = 0
dac_biet = 0
khoang_trang = 0
nguyen_am = 0
phu_am = 0

nguyen_am_set = "aeiouAEIOU"

for i in chuoi:
    if i.isalpha():
        if i.islower():
            thuong += 1
        else:
            hoa += 1

        # Kiểm tra nguyên âm / phụ âm
        if i in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

    elif i.isdigit():
        so += 1
    elif i.isspace():
        khoang_trang += 1
    else:
        dac_biet += 1

print(
    f"Chuoi co {hoa} ki tu hoa, {thuong} ki tu thuong, "
    f"{so} ki tu so, {dac_biet} ki tu dac biet, "
    f"{khoang_trang} ki tu khoang trang, "
    f"{nguyen_am} nguyen am, {phu_am} phu am"
)
