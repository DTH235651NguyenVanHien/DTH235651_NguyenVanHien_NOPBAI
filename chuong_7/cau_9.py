import json


# ================= DANH MỤC =================
def tao_danhmuc(ma, ten):
    return {"ma": ma, "ten": ten}


# ================= SẢN PHẨM =================
def tao_sanpham(ma, ten, dongia, ma_danhmuc):
    return {"ma": ma, "ten": ten, "dongia": dongia, "ma_danhmuc": ma_danhmuc}


# ================= QUẢN LÝ =================
danhmucs = []
sanphams = []


def them_danhmuc(ma, ten):
    danhmucs.append(tao_danhmuc(ma, ten))


def tim_danhmuc(ma):
    for dm in danhmucs:
        if dm["ma"] == ma:
            return dm
    return None


def them_sanpham(ma, ten, dongia, ma_danhmuc):
    if not tim_danhmuc(ma_danhmuc):
        print("Danh mục không tồn tại!")
        return
    sanphams.append(tao_sanpham(ma, ten, dongia, ma_danhmuc))


def sua_sanpham(ma, ten=None, dongia=None):
    for sp in sanphams:
        if sp["ma"] == ma:
            if ten:
                sp["ten"] = ten
            if dongia:
                sp["dongia"] = dongia
            print("Đã sửa sản phẩm")
            return
    print("Không tìm thấy sản phẩm")


def xoa_sanpham(ma):
    global sanphams
    sanphams = [sp for sp in sanphams if sp["ma"] != ma]
    print("Đã xóa sản phẩm")


def tim_sanpham(keyword):
    kq = []
    for sp in sanphams:
        if keyword.lower() in sp["ten"].lower():
            kq.append(sp)
    return kq


def sapxep_sanpham(by="ten"):
    if by == "ten":
        sanphams.sort(key=lambda sp: sp["ten"])
    elif by == "dongia":
        sanphams.sort(key=lambda sp: sp["dongia"])


# ================= FILE =================
def luu_file(filename="data.txt"):
    data = {"danhmucs": danhmucs, "sanphams": sanphams}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Đã lưu file")


def doc_file(filename="data.txt"):
    global danhmucs, sanphams
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            danhmucs = data["danhmucs"]
            sanphams = data["sanphams"]
        print("Đã đọc file")
    except FileNotFoundError:
        print("Không tìm thấy file dữ liệu")


# ================= IN THÔNG TIN =================
def in_danhmuc():
    for dm in danhmucs:
        print(f"{dm['ma']} - {dm['ten']}")


def in_sanpham():
    for sp in sanphams:
        print(f"{sp['ma']} - {sp['ten']} - {sp['dongia']} - DM:{sp['ma_danhmuc']}")


# ================= DEMO =================
if __name__ == "__main__":
    # Thêm danh mục
    them_danhmuc("DM01", "Điện thoại")
    them_danhmuc("DM02", "Laptop")

    # Thêm sản phẩm
    them_sanpham("SP01", "iPhone 15", 25000000, "DM01")
    them_sanpham("SP02", "Macbook Air", 30000000, "DM02")
    them_sanpham("SP03", "Samsung S24", 22000000, "DM01")

    # Tìm kiếm
    print("\nTìm sản phẩm 'iPhone':")
    for sp in tim_sanpham("iPhone"):
        print(sp)

    # Sắp xếp theo giá
    print("\nSản phẩm sắp xếp theo giá:")
    sapxep_sanpham("dongia")
    in_sanpham()

    # Lưu file
    luu_file()

    # Đọc file
    doc_file()
    print("\nDanh sách sản phẩm sau khi đọc file:")
    in_sanpham()
