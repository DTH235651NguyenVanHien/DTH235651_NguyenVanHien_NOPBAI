import json


# ================== TẠO DỮ LIỆU ==================
def tao_lop(ma_lop, ten_lop):
    return {"ma_lop": ma_lop, "ten_lop": ten_lop}


def tao_sinhvien(ma_sv, ten_sv, nam_sinh, ma_lop):
    return {"ma_sv": ma_sv, "ten_sv": ten_sv, "nam_sinh": nam_sinh, "ma_lop": ma_lop}


# ================== QUẢN LÝ ==================
lops = []
sinhviens = []


# ----- LỚP -----
def them_lop(ma, ten):
    lops.append(tao_lop(ma, ten))


def tim_lop(ma):
    for lop in lops:
        if lop["ma_lop"] == ma:
            return lop
    return None


# ----- SINH VIÊN -----
def them_sinhvien(ma_sv, ten_sv, nam_sinh, ma_lop):
    if not tim_lop(ma_lop):
        print("Lớp không tồn tại!")
        return
    sinhviens.append(tao_sinhvien(ma_sv, ten_sv, nam_sinh, ma_lop))


def sua_sinhvien(ma_sv, ten=None, nam_sinh=None):
    for sv in sinhviens:
        if sv["ma_sv"] == ma_sv:
            if ten:
                sv["ten_sv"] = ten
            if nam_sinh:
                sv["nam_sinh"] = nam_sinh
            print("Đã sửa sinh viên")
            return
    print("Không tìm thấy sinh viên")


def xoa_sinhvien(ma_sv):
    global sinhviens
    truoc = len(sinhviens)
    sinhviens = [sv for sv in sinhviens if sv["ma_sv"] != ma_sv]
    if len(sinhviens) < truoc:
        print("Đã xóa sinh viên")
    else:
        print("Không tìm thấy sinh viên")


def tim_sinhvien(keyword):
    kq = []
    for sv in sinhviens:
        if keyword.lower() in sv["ten_sv"].lower():
            kq.append(sv)
    return kq


def sapxep_sinhvien(by="ten"):
    if by == "ten":
        sinhviens.sort(key=lambda sv: sv["ten_sv"])
    elif by == "namsinh":
        sinhviens.sort(key=lambda sv: sv["nam_sinh"])


# ================== FILE ==================
def luu_file(filename="sinhvien.json"):
    data = {"lops": lops, "sinhviens": sinhviens}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Đã lưu file")


def doc_file(filename="sinhvien.json"):
    global lops, sinhviens
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            lops = data["lops"]
            sinhviens = data["sinhviens"]
        print("Đã đọc file")
    except FileNotFoundError:
        print("Chưa có file dữ liệu")


# ================== DEMO ==================
if __name__ == "__main__":
    # Thêm lớp
    them_lop("CTK44A", "Công nghệ thông tin 44A")
    them_lop("CTK44B", "Công nghệ thông tin 44B")

    # Thêm sinh viên
    them_sinhvien("SV01", "Nguyễn Văn A", 2004, "CTK44A")
    them_sinhvien("SV02", "Trần Thị B", 2003, "CTK44B")
    them_sinhvien("SV03", "Lê Văn C", 2005, "CTK44A")

    # Tìm kiếm
    print("\nTìm sinh viên 'Nguyễn':")
    for sv in tim_sinhvien("Nguyễn"):
        print(sv)

    # Sắp xếp
    print("\nDanh sách sinh viên sắp xếp theo năm sinh:")
    sapxep_sinhvien(by="namsinh")
    for sv in sinhviens:
        print(sv)

    # Lưu file
    luu_file()

    # Đọc lại file
    doc_file()
    print("\nDanh sách sinh viên sau khi đọc file:")
    for sv in sinhviens:
        print(sv)
