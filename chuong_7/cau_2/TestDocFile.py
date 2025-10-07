from XuLyFile import *

arrSo = DocFile("chuong_7/bai_2/csdl_so.txt")
print(arrSo)


def XuatSoAmTrenMoiDong(arrSo):
    for row in arrSo:
        for element in row:
            number = int(element)
        if number < 0:
            print(number, end="\t")
    print()


print("Các số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)
