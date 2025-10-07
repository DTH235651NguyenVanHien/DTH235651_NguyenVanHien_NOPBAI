def nhap_ma_tran():
    print("Nhap ma tran: ")
    hang = int(input("Nhap so hang: "))
    cot = int(input("Nhap so cot: "))
    matran = []
    for i in range(hang):
        hang_moi = []
        for j in range(cot):
            so = int(input(f"Nhap phan tu [{i}][{j}]: "))
            hang_moi.append(so)
        matran.append(hang_moi)
    return matran


def in_ma_tran(m):
    for hand in range(len(m)):
        for cot in range(len(m[0])):
            print(m[hand][cot], end=" ")
        print()


def cong_ma_tran(a, b):
    ket_qua = []
    for i in range(len(a)):
        hang_moi = []
        for j in range(len(a[0])):
            hang_moi.append(a[i][j] + b[i][j])
        ket_qua.append(hang_moi)
    return ket_qua

def hoan_vi_matran(m):
    hang = len(m)
    cot = len(m[0])
    ketqua = []
    for j in range(cot):
        hang_moi = []
        for i in range(hang):
            hang_moi.append(m[i][j])
        ketqua.append(hang_moi)
    return ketqua

a = nhap_ma_tran()
b = nhap_ma_tran()

print("Ma tran A: ")
in_ma_tran(a)

print("Ma tran B: ")
in_ma_tran(b)

print("Ma tran A + B: ")
in_ma_tran(cong_ma_tran(a, b))

print("Ma tran A hoan vi: ")
in_ma_tran(hoan_vi_matran(a))

print("Ma tran B hoan vi: ")
in_ma_tran(hoan_vi_matran(b))