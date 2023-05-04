from fontTools import ttLib

t = ttLib.TTFont(input("Input font filename: "))

zhihu_dict = {}

for x in t["cmap"].tables[0].cmap.items():
    zhihu_dict[chr(x[0])] = chr(int(x[1][3:], 16))

print(zhihu_dict)
