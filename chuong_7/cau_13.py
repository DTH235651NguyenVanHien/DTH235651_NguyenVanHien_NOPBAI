import xml.etree.ElementTree as ET
from collections import defaultdict


class Nhom:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

    def __str__(self):
        return f"{self.ma} - {self.ten}"


class ThietBi:
    def __init__(self, ma, ten, ma_nhom):
        self.ma = ma
        self.ten = ten
        self.ma_nhom = ma_nhom

    def __str__(self):
        return f"{self.ma} - {self.ten} (Nhóm: {self.ma_nhom})"


class QuanLyThietBi:
    def __init__(self):
        self.nhoms = []
        self.thietbis = []

    # ===== ĐỌC FILE XML =====
    def doc_nhom(self, filename="nhomthietbi.xml"):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.nhoms.clear()
        for nhom in root.findall("nhom"):
            ma = nhom.find("ma").text
            ten = nhom.find("ten").text
            self.nhoms.append(Nhom(ma, ten))

    def doc_thietbi(self, filename="ThietBi.xml"):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.thietbis.clear()
        for tb in root.findall("thietbi"):
            ma_nhom = tb.get("manhom")
            ma = tb.find("ma").text
            ten = tb.find("ten").text
            self.thietbis.append(ThietBi(ma, ten, ma_nhom))

    # ===== HIỂN THỊ =====
    def hien_thi_nhom(self):
        print("\n📂 Danh sách Nhóm thiết bị:")
        for n in self.nhoms:
            print("-", n)

    def hien_thi_thietbi(self):
        print("\n📋 Danh sách Thiết bị:")
        for tb in self.thietbis:
            print("-", tb)

    def loc_thietbi_theo_nhom(self, ma_nhom):
        print(f"\n🔍 Danh sách Thiết bị thuộc nhóm {ma_nhom}:")
        for tb in self.thietbis:
            if tb.ma_nhom == ma_nhom:
                print("-", tb)

    def nhom_nhieu_thietbi_nhat(self):
        counter = defaultdict(int)
        for tb in self.thietbis:
            counter[tb.ma_nhom] += 1

        if not counter:
            print("⚠️ Chưa có dữ liệu thiết bị")
            return

        max_nhom = max(counter, key=counter.get)
        so_luong = counter[max_nhom]

        # Lấy tên nhóm
        ten_nhom = next((n.ten for n in self.nhoms if n.ma == max_nhom), max_nhom)

        print(f"\n🏆 Nhóm có nhiều thiết bị nhất: {ten_nhom} ({so_luong} thiết bị)")


if __name__ == "__main__":
    ql = QuanLyThietBi()

    # Đọc dữ liệu từ XML
    ql.doc_nhom("nhomthietbi.xml")
    ql.doc_thietbi("ThietBi.xml")

    # Hiển thị nhóm
    ql.hien_thi_nhom()

    # Hiển thị thiết bị
    ql.hien_thi_thietbi()

    # Lọc thiết bị theo nhóm
    ql.loc_thietbi_theo_nhom("n3")

    # Nhóm có nhiều thiết bị nhất
    ql.nhom_nhieu_thietbi_nhat()
