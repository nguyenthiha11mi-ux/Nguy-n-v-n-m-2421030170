n = int(input("Nhập số phần tử n: "))

while n <= 0 or n >= 100:
    n = int(input("Nhập lại n (0 < n < 100): "))

tong = 0
dem = 0

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    
    if -1000 < x < -10:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print("Trung bình cộng các phần tử thỏa mãn là:", tbc)
else:
    print("Không có phần tử nào thỏa mãn")