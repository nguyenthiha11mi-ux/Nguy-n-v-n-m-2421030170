

print("=== BTVN1 - TONG CAC SO CHAN ===")
tong = 0

while True:
    so = int(input("Nhap so (nhap 0 de dung): "))
    if so == 0:
        break
    if so % 2 == 0:
        tong += so

print("Tong cac so chan:", tong)
