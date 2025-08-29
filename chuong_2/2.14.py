# 14. Một ngày thứ tư đẹp trời, bạn đi du lịch tại một hòn đảo rất đẹp. Bạn đã ngủ lại đó hết 137 đêm. Hỏi bạn về nhà vào ngày thứ mấy trong tuần? Hãy viết chương trình bằng Python để tỉnh.

thu_trong_tuan = ["Thu 2", "Thu 3", "Thu 4", "Thu 5", "Thu 6", "Thu 7", "Chu nhat"]
thu_bat_dau = 2 # Thu 4 trong mang thu_trong_tuan

thu_ve = (thu_bat_dau + 137) % 7

print(thu_trong_tuan[thu_ve])