def checkdoixung(s):
  return s == s[::-1]

def main():
  s = input("Nhap vao chuoi: ")
  if checkdoixung(s):
    print("Chuoi doi xung")
  else:
    print("Chuoi khong doi xung")

while True:
  main()
  print("Ban muon nhap tiep khong? (y/n): ")
  s = input()
  if s == "k": break

print("Cam on ban da su dung chuong trinh")