so_sao = [1, 3, 5, 3, 5, 7, 1, 3]

chieu_rong = max(so_sao)  

for n in so_sao:
    khoang_trang = (chieu_rong - n) // 2
    print(" " * khoang_trang + "*" * n)