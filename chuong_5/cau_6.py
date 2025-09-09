def NegativeNumberInStrings(s: str):
    nums = []
    i = 0
    while i < len(s):
        if s[i] == "-" and i + 1 < len(s) and s[i + 1].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            nums.append(int(s[i:j]))  # cắt từ i đến j
            i = j  # nhảy qua đoạn số
        else:
            i += 1
    return nums

s = "abc-5xyz-12k9l--p"
result = NegativeNumberInStrings(s)
print("Các số nguyên âm tìm được:", result)
