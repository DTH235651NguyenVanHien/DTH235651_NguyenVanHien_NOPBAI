import random
import csv


# Hàm lưu file CSV
def luu_csv(filename="data.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        for _ in range(10):  # 10 dòng
            row = [random.randint(1, 100) for _ in range(10)]  # 10 số ngẫu nhiên
            writer.writerow(row)
    print(f"💾 Đã lưu file {filename}")


# Hàm đọc file CSV và tính tổng từng dòng
def doc_csv(filename="data.csv"):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for i, row in enumerate(reader, start=1):
            numbers = [int(x) for x in row if x.strip() != ""]
            tong = sum(numbers)
            print(f"Dòng {i}: {row} ➝ Tổng = {tong}")


# ===================== DEMO =====================

if __name__ == "__main__":
    luu_csv("data.csv")
    doc_csv("data.csv")
