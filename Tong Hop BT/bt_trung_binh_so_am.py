# Nhap day so thuc, tinh TBC cac phan tu am trong khoang (-1000, -10)

print("=== BT - TRUNG BINH CAC SO AM ===")
n = int(input("Nhap n: "))

tong = 0
dem = 0
for i in range(n):
    x = float(input(f"Nhap x{i+1}: "))
    if -1000 < x < -10:
        tong += x
        dem += 1

if dem > 0:
    print(f"So phan tu thoa man: {dem}")
    print(f"TBC cac phan tu am trong (-1000, -10): {tong / dem}")
else:
    print("Khong co phan tu nao thoa man")
