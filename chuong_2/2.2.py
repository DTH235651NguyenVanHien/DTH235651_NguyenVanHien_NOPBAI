# 2. Viết chương trình cho người dùng nhập vào từ bàn phím hai số a, b và một ký tự ch. Kiểm tra, nếu: ch là + thì thực hiện phép tính a + b và in kết quả lên màn hình, nếu ch là " thì thực hiện phép tính a - b và in kết quả lên màn hình, nếu ch là *** thi thực hiện phép tính a* b và in kết quả lên màn hình, nếu ch là / thì thực hiện phép tỉnh a / b và ín kết quả lên màn hình, nếu ch là ký tự khác các ký tự trên thì hiển thị ra màn hình ký tự ch không phải là một toán từ.

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
ch = input("Nhap ch: ")

if ch == "+":
    print(f"{a} {ch} {b} = {a + b}")
elif ch == "-":
    print(f"{a} {ch} {b} = {a - b}")
elif ch == "*":
    print(f"{a} {ch} {b} = {a * b}")
elif ch == "/":
    if b == 0:
        print("Khong the chia cho 0")
    else:
        print(f"{a} {ch} {b} = {a / b}")
else:
    print(f"{ch} khong phai la mot toan tu")
