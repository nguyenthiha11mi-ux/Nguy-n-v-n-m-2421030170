x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
z = int(input("Nhap z: "))
tich = x * y * z
so_chu_so = len(str(tich))
lon_nhat = 0
for ky_tu in str(tich):
    if int(ky_tu) > lon_nhat:
        lon_nhat = int(ky_tu)
print(f"Tich x*y*z: {tich}")
print(f"So chu so: {so_chu_so}")
print(f"Chu so lon nhat: {lon_nhat}")
