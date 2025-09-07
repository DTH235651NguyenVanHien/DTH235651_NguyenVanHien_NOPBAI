hang = 4
cot = 4

for i in range(1, hang + 1):
    for j in range(1, cot + 1):
        if i == 1 or i == 4 or j == 1 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
