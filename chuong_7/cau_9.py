import json


class Category:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

    def __str__(self):
        return f"{self.ma} - {self.ten}"


class Product:
    def __init__(self, ma, ten, dongia, ma_danhmuc):
        self.ma = ma
        self.ten = ten
        self.dongia = dongia
        self.ma_danhmuc = ma_danhmuc

    def __str__(self):
        return f"{self.ma} - {self.ten} - {self.dongia} - DM:{self.ma_danhmuc}"


class QuanLy:
    def __init__(self):
        self.danhmucs = []
        self.sanphams = []

    # ===== DANH MỤC =====
    def them_danhmuc(self, ma, ten):
        self.danhmucs.append(Category(ma, ten))

    def tim_danhmuc(self, ma):
        return next((dm for dm in self.danhmucs if dm.ma == ma), None)

    # ===== SẢN PHẨM =====
    def them_sanpham(self, ma, ten, dongia, ma_danhmuc):
        if not self.tim_danhmuc(ma_danhmuc):
            print("❌ Danh mục không tồn tại!")
            return
        self.sanphams.append(Product(ma, ten, dongia, ma_danhmuc))

    def sua_sanpham(self, ma, ten=None, dongia=None):
        sp = next((sp for sp in self.sanphams if sp.ma == ma), None)
        if sp:
            if ten:
                sp.ten = ten
            if dongia:
                sp.dongia = dongia
            print("✅ Sửa thành công")
        else:
            print("❌ Không tìm thấy sản phẩm")

    def xoa_sanpham(self, ma):
        self.sanphams = [sp for sp in self.sanphams if sp.ma != ma]
        print("✅ Xóa thành công")

    def tim_sanpham(self, keyword):
        return [sp for sp in self.sanphams if keyword.lower() in sp.ten.lower()]

    def sapxep_sanpham(self, by="ten"):
        if by == "ten":
            self.sanphams.sort(key=lambda sp: sp.ten)
        elif by == "dongia":
            self.sanphams.sort(key=lambda sp: sp.dongia)

    # ===== LƯU / ĐỌC FILE =====
    def save_file(self, filename="data.txt"):
        data = {
            "danhmucs": [dm.__dict__ for dm in self.danhmucs],
            "sanphams": [sp.__dict__ for sp in self.sanphams],
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("💾 Đã lưu file")

    def load_file(self, filename="data.txt"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.danhmucs = [Category(**dm) for dm in data["danhmucs"]]
                self.sanphams = [Product(**sp) for sp in data["sanphams"]]
            print("📂 Đã đọc file")
        except FileNotFoundError:
            print("⚠️ Chưa có file dữ liệu")


# ===================== DEMO =====================

if __name__ == "__main__":
    ql = QuanLy()

    # Thêm danh mục
    ql.them_danhmuc("DM01", "Điện thoại")
    ql.them_danhmuc("DM02", "Laptop")

    # Thêm sản phẩm
    ql.them_sanpham("SP01", "iPhone 15", 25000000, "DM01")
    ql.them_sanpham("SP02", "Macbook Air", 30000000, "DM02")
    ql.them_sanpham("SP03", "Samsung S24", 22000000, "DM01")

    # Tìm kiếm
    print("\n🔍 Tìm sản phẩm 'iPhone':")
    for sp in ql.tim_sanpham("iPhone"):
        print(sp)

    # Sắp xếp
    print("\n📌 Sản phẩm sắp xếp theo giá:")
    ql.sapxep_sanpham(by="dongia")
    for sp in ql.sanphams:
        print(sp)

    # Lưu file
    ql.save_file()

    # Đọc lại file
    ql2 = QuanLy()
    ql2.load_file()
    print("\n📂 Danh sách sản phẩm sau khi đọc file:")
    for sp in ql2.sanphams:
        print(sp)
