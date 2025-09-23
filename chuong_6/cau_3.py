from random import randrange

def TaoMaTran(m, n):
  D = []
  for i in range(m):
    row = []
    for j in range(n):
      row.append(randrange(100))
    D.append(row)
  return D

def XuatMaTran(D):
  for row in D:
    for element in row:
      print(element, end="\t")
    print()

def LayDong(r):
  R = D[r]
  return R

def XuatList1Chieu(R):
  for element in R:
    print(element, end="\t")
  print()

def LayCot(c):
  C = []
  for i in range(len(D)):
    C.append(D[i][c])
  return C

def MAX(D):
  max = D[0][0]
  for i in range(len(D)):
    for j in range(len(D[i])):
      if D[i][j] > max:
        max = D[i][j]
  return max

m = int(input("Nhap so dong: "))
n = int(input("Nhap so cot: "))
D = TaoMaTran(m, n)
XuatMaTran(D)
r = int(input("Nhap dong can tim: "))
R = LayDong(r)
XuatList1Chieu(R)
c = int(input("Nhap cot can tim: "))
C = LayCot(c)
XuatList1Chieu(C)
print("Gia tri lon nhat trong ma tran la: ", MAX(D))