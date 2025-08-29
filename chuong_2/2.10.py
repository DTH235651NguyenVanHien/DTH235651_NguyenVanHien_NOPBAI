# 10. Viết chương trình in ra màn hình bảng cửu chương từ 2-9

for i in range(1, 11):
    for j in range(2, 11):
        print(f"{j} x {i} = {j*i}", end="\t")
    print()
