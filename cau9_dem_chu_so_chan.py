a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
tong = a + b + c
dem = 0
for ky_tu in str(tong):
    if int(ky_tu) % 2 == 0:
        dem += 1
print(f"Tong a+b+c: {tong}")
print(f"So chu so chan trong tong: {dem}")
