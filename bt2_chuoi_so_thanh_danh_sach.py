

print("=== BT2 - CHUOI SO THANH DANH SACH ===")
chuoi = input("Nhap chuoi so (VD: 2 4 6 7 9): ")

danh_sach = []
for so in chuoi.split():
    danh_sach.append(int(so))

print("Mang:", danh_sach)
