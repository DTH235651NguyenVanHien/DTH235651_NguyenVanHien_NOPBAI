# 5. Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ. Ví dụ: n=35 => Ba mươi lăm, n=5 => năm).


def doc_so(n):
    hang_chuc = [
        "",
        "muoi",
        "hai muoi",
        "ba muoi",
        "bon muoi",
        "nam muoi",
        "sau muoi",
        "bay muoi",
        "tam muoi",
        "chin muoi",
    ]
    hang_don_vi = [
        "khong",
        "mot",
        "hai",
        "ba",
        "bon",
        "nam",
        "sau",
        "bay",
        "tam",
        "chin",
    ]

    if n < 10:
        return hang_don_vi[n]
    else:
        hang_chuc_so = n // 10
        hang_don_vi_so = n % 10
        if hang_don_vi_so == 0:
            return hang_chuc[hang_chuc_so]
        elif hang_don_vi_so == 1:
            return hang_chuc[hang_chuc_so] + " mot"
        elif hang_don_vi_so == 5:
            return hang_chuc[hang_chuc_so] + " lam"
        else:
            return hang_chuc[hang_chuc_so] + " " + hang_don_vi[hang_don_vi_so]


so_can_doc = int(input("Nhap so can doc: "))

if so_can_doc < 0:
    print(f"Am {doc_so(abs(so_can_doc))}")
else:
    print(doc_so(so_can_doc))
