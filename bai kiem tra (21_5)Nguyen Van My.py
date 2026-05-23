# c1
# Nhap day so thuc, tinh trung binh cong cac phan tu duong trong khoang (0, 1000)

print("CAU 1")
n = int(input("Nhap n: "))
tong = 0
dem = 0
for i in range(n):
    x = float(input(f"Nhap x{i+1}: "))
    if x > 0 and x < 1000:
        tong += x
        dem += 1

if dem > 0:
    print(f"Trung binh cong: {tong / dem}")
else:
    print("Khong co phan tu nao thoa man")


# c2
# Kiem tra tong cac chu so cua n co chia het cho 3 hay khong

print("\CAU 2")
n = int(input("Nhap so nguyen duong n: "))
tong = 0
tam = n
while tam > 0:
    tong += tam % 10
    tam //= 10

if tong % 3 == 0:
    print(f"Tong cac chu so = {tong}, chia het cho 3")
else:
    print(f"Tong cac chu so = {tong}, khong chia het cho 3")


# c3
# Kiem tra tich cac chu so cua n co phai so chan va lon hon 20 hay khong

print("\n=== CAU 3 ===")
n = int(input("Nhap so nguyen duong n: "))
tich = 1
tam = n
while tam > 0:
    tich *= tam % 10
    tam //= 10

if tich % 2 == 0 and tich > 20:
    print(f"Tich cac chu so = {tich}, la so chan va lon hon 20")
else:
    print(f"Tich cac chu so = {tich}, khong thoa man dieu kien")


# c4
# Tinh tong (a+b), tim chu so lon nhat trong tong

print("\n=== CAU 4 ===")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
tong = a + b
print(f"Tong a + b = {tong}")

lon_nhat = 0
tam = tong
while tam > 0:
    chu_so = tam % 10
    if chu_so > lon_nhat:
        lon_nhat = chu_so
    tam //= 10

print(f"Chu so lon nhat trong {tong} la: {lon_nhat}")


# c5
# Kiem tra m co chia het cho tong cac chu so cua n hay khong

print("\n=== CAU 5 ===")
m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

tong = 0
tam = n
while tam > 0:
    tong += tam % 10
    tam //= 10

print(f"Tong cac chu so cua {n} = {tong}")

if tong == 0:
    print("Tong chu so bang 0, khong chia duoc")
elif m % tong == 0:
    print(f"{m} chia het cho {tong}")
else:
    print(f"{m} khong chia het cho {tong}")
