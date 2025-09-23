from XuLyFile import *

masp = input("Nhap ma san pham: ")
tensp = input("Nhap ten san pham: ")
dongia = float(input("Nhap don gia: "))
line = masp + ";" + tensp + ";" + str(dongia)

LuuFile("chuong_7/bai_1/database.txt", line)