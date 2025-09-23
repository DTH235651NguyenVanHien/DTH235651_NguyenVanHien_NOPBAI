import openpyxl
from openpyxl import Workbook


class NhanVien:
    def __init__(self, ma, ten, tuoi):
        self.ma = ma
        self.ten = ten
        self.tuoi = tuoi

    def __str__(self):
        return f"{self.ma} - {self.ten} - {self.tuoi}"


class QuanLyNhanVien:
    def __init__(self):
        self.nhanviens = []

    def them_nv(self, ma, ten, tuoi):
        self.nhanviens.append(NhanVien(ma, ten, tuoi))

    def sapxep_theo_tuoi(self):
        self.nhanviens.sort(key=lambda nv: nv.tuoi)

    def luu_excel(self, filename="nhanvien.xlsx"):
        wb = Workbook()
        ws = wb.active
        ws.title = "DanhSachNV"

        # Ghi tiêu đề
        ws.append(["Mã", "Tên", "Tuổi"])

        # Ghi dữ liệu
        for nv in self.nhanviens:
            ws.append([nv.ma, nv.ten, nv.tuoi])

        wb.save(filename)
        print(f"💾 Đã lưu danh sách nhân viên vào file {filename}")

    def doc_excel(self, filename="nhanvien.xlsx"):
        try:
            wb = openpyxl.load_workbook(filename)
            ws = wb.active
            self.nhanviens.clear()

            for row in ws.iter_rows(min_row=2, values_only=True):  # bỏ dòng tiêu đề
                ma, ten, tuoi = row
                self.nhanviens.append(NhanVien(ma, ten, tuoi))

            print(f"📂 Đã đọc {len(self.nhanviens)} nhân viên từ file {filename}")
        except FileNotFoundError:
            print("⚠️ Chưa có file Excel dữ liệu")


# ===================== DEMO =====================

if __name__ == "__main__":
    ql = QuanLyNhanVien()

    # Thêm nhân viên
    ql.them_nv("NV01", "Nguyễn Văn A", 25)
    ql.them_nv("NV02", "Trần Thị B", 30)
    ql.them_nv("NV03", "Lê Văn C", 22)

    # Lưu file Excel
    ql.luu_excel()

    # Đọc lại file Excel
    ql2 = QuanLyNhanVien()
    ql2.doc_excel()

    # In danh sách nhân viên
    print("\n📋 Danh sách nhân viên:")
    for nv in ql2.nhanviens:
        print(nv)

    # Sắp xếp theo tuổi
    ql2.sapxep_theo_tuoi()
    print("\n📌 Danh sách nhân viên theo tuổi tăng dần:")
    for nv in ql2.nhanviens:
        print(nv)
