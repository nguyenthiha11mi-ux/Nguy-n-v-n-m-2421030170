m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
tong = m + n
lon_nhat = 0
for ky_tu in str(tong):
    if int(ky_tu) > lon_nhat:
        lon_nhat = int(ky_tu)
print(f"Tong: {tong}")
print(f"Chu so lon nhat: {lon_nhat}")
