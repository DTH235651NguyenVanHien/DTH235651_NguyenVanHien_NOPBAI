n = int(input("Nhap vao so nguyen duong n: "))

def doc_hai_chu_so(n):
  chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
  don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chin"]

  if n < 10:
    return don_vi[n]

  hang_chuc_so = n // 10
  hang_don_vi_so = n % 10

  if hang_don_vi_so == 0:
    return chuc[hang_chuc_so]
  elif hang_don_vi_so == 1:
    if hang_chuc_so == 1:
      return chuc[hang_chuc_so] + " một"
    else:
      return chuc[hang_chuc_so] + " mốt"
  elif hang_don_vi_so == 5:
    return chuc[hang_chuc_so] + " lăm"
  else:
    return chuc[hang_chuc_so] + " " + don_vi[hang_don_vi_so]
  
print(doc_hai_chu_so(n))

  