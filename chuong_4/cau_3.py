def BMI (height, weight):
  return weight / height ** 2

def PhanLoai (bmi):
  if bmi < 18.5:
    return "gay"
  elif bmi <= 24.9:
    return "Binh thuong"
  elif bmi <= 34.9:
    return "Beo phi cap 1"
  elif bmi <= 39.9:
    return "Beo phi cap 2"
  else:
    return "Beo phi cap 3"
  
def NguyCoBenh (bmi):
  if bmi < 18.5:
    return "Thap"
  elif bmi <= 24.9:
    return "Trung binh"
  elif bmi <= 34.9:
    return "Cao"
  elif bmi <= 39.9:
    return "Rat cao"
  else:
    return "Nguy hiem"
  
print("Nhap vao chieu cao: ")
height = float(input())
print("Nhap vao can nang: ")
weight = float(input())

bmi = BMI(height, weight)
print("BMI cua ban la: ", bmi)
print("Phan loai cua ban la: ", PhanLoai(bmi))
print("Nguy co benh cua ban la: ", NguyCoBenh(bmi))