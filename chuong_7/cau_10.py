import json


class Lop:
    def __init__(self, ma_lop, ten_lop):
        self.ma_lop = ma_lop
        self.ten_lop = ten_lop

    def __str__(self):
        return f"{self.ma_lop} - {self.ten_lop}"


class SinhVien:
    def __init__(self, ma_sv, ten_sv, nam_sinh, ma_lop):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.nam_sinh = nam_sinh
        self.ma_lop = ma_lop

    def __str__(self):
        return f"{self.ma_sv} - {self.ten_sv} - {self.nam_sinh} - Lớp:{self.ma_lop}"


class QuanLySinhVien:
    def __init__(self):
        self.lops = []
        self.sinhviens = []

    # ===== LỚP =====
    def them_lop(self, ma, ten):
        self.lops.append(Lop(ma, ten))

    def tim_lop(self, ma):
        return next((lop for lop in self.lops if lop.ma_lop == ma), None)

    # ===== SINH VIÊN =====
    def them_sinhvien(self, ma_sv, ten_sv, nam_sinh, ma_lop):
        if not self.tim_lop(ma_lop):
            print("❌ Lớp không tồn tại!")
            return
        self.sinhviens.append(SinhVien(ma_sv, ten_sv, nam_sinh, ma_lop))

    def sua_sinhvien(self, ma_sv, ten=None, nam_sinh=None):
        sv = next((sv for sv in self.sinhviens if sv.ma_sv == ma_sv), None)
        if sv:
            if ten:
                sv.ten_sv = ten
            if nam_sinh:
                sv.nam_sinh = nam_sinh
            print("✅ Sửa thành công")
        else:
            print("❌ Không tìm thấy sinh viên")

    def xoa_sinhvien(self, ma_sv):
        before = len(self.sinhviens)
        self.sinhviens = [sv for sv in self.sinhviens if sv.ma_sv != ma_sv]
        if len(self.sinhviens) < before:
            print("✅ Xóa thành công")
        else:
            print("❌ Không tìm thấy sinh viên")

    def tim_sinhvien(self, keyword):
        return [sv for sv in self.sinhviens if keyword.lower() in sv.ten_sv.lower()]

    def sapxep_sinhvien(self, by="ten"):
        if by == "ten":
            self.sinhviens.sort(key=lambda sv: sv.ten_sv)
        elif by == "namsinh":
            self.sinhviens.sort(key=lambda sv: sv.nam_sinh)

    # ===== LƯU / ĐỌC FILE =====
    def save_file(self, filename="sinhvien.json"):
        data = {
            "lops": [lop.__dict__ for lop in self.lops],
            "sinhviens": [sv.__dict__ for sv in self.sinhviens],
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("💾 Đã lưu file")

    def load_file(self, filename="sinhvien.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.lops = [Lop(**lop) for lop in data["lops"]]
                self.sinhviens = [SinhVien(**sv) for sv in data["sinhviens"]]
            print("📂 Đã đọc file")
        except FileNotFoundError:
            print("⚠️ Chưa có file dữ liệu")


# ===================== DEMO =====================

if __name__ == "__main__":
    ql = QuanLySinhVien()

    # Thêm lớp
    ql.them_lop("CTK44A", "Công nghệ thông tin 44A")
    ql.them_lop("CTK44B", "Công nghệ thông tin 44B")

    # Thêm sinh viên
    ql.them_sinhvien("SV01", "Nguyễn Văn A", 2004, "CTK44A")
    ql.them_sinhvien("SV02", "Trần Thị B", 2003, "CTK44B")
    ql.them_sinhvien("SV03", "Lê Văn C", 2005, "CTK44A")

    # Tìm kiếm
    print("\n🔍 Tìm sinh viên 'Nguyễn':")
    for sv in ql.tim_sinhvien("Nguyễn"):
        print(sv)

    # Sắp xếp
    print("\n📌 Danh sách sinh viên sắp xếp theo năm sinh:")
    ql.sapxep_sinhvien(by="namsinh")
    for sv in ql.sinhviens:
        print(sv)

    # Lưu file
    ql.save_file()

    # Đọc lại file
    ql2 = QuanLySinhVien()
    ql2.load_file()
    print("\n📂 Danh sách sinh viên sau khi đọc file:")
    for sv in ql2.sinhviens:
        print(sv)
