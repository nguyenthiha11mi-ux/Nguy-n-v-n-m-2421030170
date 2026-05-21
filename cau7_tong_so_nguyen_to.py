n = int(input("Nhap n: "))
tong = 0
for i in range(n):
    x = int(input(f"Nhap x{i+1}: "))
    if x < 2:
        continue
    la_nto = True
    for j in range(2, x):
        if x % j == 0:
            la_nto = False
            break
    if la_nto:
        tong += x
if tong % 2 != 0 and tong > 50:
    print(f"Tong so nguyen to: {tong}, la so le va lon hon 50")
else:
    print(f"Tong so nguyen to: {tong}, khong thoa man dieu kien")
