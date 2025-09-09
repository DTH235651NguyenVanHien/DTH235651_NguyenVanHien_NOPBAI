def ToiUuChuoi(s):
    s2 = s
    s2 = s2.strip()
    s2 = s2.split("\\s+")
    return " ".join(s2)


s = " Trần Duy Thanh "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))
