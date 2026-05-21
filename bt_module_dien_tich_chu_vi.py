# Module 1: Cac ham tinh dien tich, chu vi
# Module 2: Goi ham tu module 1 va in ket qua

print("=== BT MODULE - TINH DIEN TICH CHU VI ===")

def dien_tich_hcn(dai, rong):
    return dai * rong

def dien_tich_hvuong(canh):
    return canh * canh

def dien_tich_htron(ban_kinh):
    return 3.14 * ban_kinh * ban_kinh

def chu_vi_hcn(dai, rong):
    return 2 * (dai + rong)

print("\n-- Hinh chu nhat --")
dai = float(input("Nhap chieu dai: "))
rong = float(input("Nhap chieu rong: "))
print("Dien tich HCN:", dien_tich_hcn(dai, rong))
print("Chu vi HCN:", chu_vi_hcn(dai, rong))

print("\n-- Hinh vuong --")
canh = float(input("Nhap canh: "))
print("Dien tich H.Vuong:", dien_tich_hvuong(canh))

print("\n-- Hinh tron --")
r = float(input("Nhap ban kinh: "))
print("Dien tich H.Tron:", dien_tich_htron(r))
