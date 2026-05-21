a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
nho_nhat = 9
for ky_tu in str(b):
    if int(ky_tu) < nho_nhat:
        nho_nhat = int(ky_tu)
if nho_nhat == 0:
    print("Chu so nho nhat cua b la 0, khong chia duoc")
elif a % nho_nhat == 0:
    print(f"Chu so nho nhat cua b la {nho_nhat}, {a} chia het cho {nho_nhat}")
else:
    print(f"Chu so nho nhat cua b la {nho_nhat}, {a} khong chia het cho {nho_nhat}")
