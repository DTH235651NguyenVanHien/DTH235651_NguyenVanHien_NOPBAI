from random import randrange

while True:
  somay = randrange(1, 101)
  solandoan = 0
  win = False
  while solandoan < 7:
    solandoan += 1
    songuoi = int(input("May doan [1...100], moi ban doan: "))
    print("Ban doan lan thu: ", solandoan)
    if somay == songuoi:
      print("Chuc mung ban doan dung, so may la = ", somay)
      win = True
      break
    if somay < songuoi:
      print("Ban doan sai, so may > so ban")
    elif somay < songuoi:
      print("Ban doan sai, so may < so ban")
  
  if win == False:
    print("GAME OVER, so may la = ", somay)
  hoi = input("Ban muon choi tiep khong? (y/n): ")
  if hoi == "k":
    break
print("Cam on ban da choi GAME!")