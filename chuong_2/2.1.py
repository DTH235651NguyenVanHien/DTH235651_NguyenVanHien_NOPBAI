# 1. Giả sử một người A có số tiền bằng X, đem gửi tiết kiệm với lãi suất tháng là 0,6%; hỏi rằng sau 18 tháng thì A có tất cả bao nhiêu tiền? Hãy viết chương trình cho người dùng nhập vào số tiền X sau đô tỉnh tổng tiền sau 18 tháng. Biết rằng cứ 6 tháng thì tiền lãi được cộng vào gốc và người A không rút tiền.

lai_suat_thang = 0.006
tong_thang_gui = 18
chu_ky_tinh_lai = 6

so_tien_ban_dau = float(input("Nhập số tiền gửi tiết kiệm ban đầu: "))

so_chu_ky = tong_thang_gui // chu_ky_tinh_lai

tong_tien = so_tien_ban_dau * (1 + lai_suat_thang * chu_ky_tinh_lai) ** so_chu_ky

print("Số tiền có được sau 18 tháng là:", round(tong_tien, 2))
