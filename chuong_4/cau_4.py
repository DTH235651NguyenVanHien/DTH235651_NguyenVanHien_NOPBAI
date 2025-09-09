def ROI(dt, cp):
    return (dt - cp) / cp

def GoiYDauTu (roi):
    if roi >= 0.75:
        return "Nen dau tu"
    else:
        return "Khong nen dau tu"
    
print("Chuong trinh tinh ROI")
dt = float(input("Nhap vao doanh thu: "))
cp = float(input("Nhap vao chi phi: "))
roi = ROI(dt, cp)
print(f"ROI la: {roi}")
print(GoiYDauTu(roi))