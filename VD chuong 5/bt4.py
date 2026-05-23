m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

tong = m + n

print("Tổng =", tong)

temp = tong
max_cs = 0

while temp > 0:
    cs = temp % 10
    
    if cs > max_cs:
        max_cs = cs
        
    temp = temp // 10

print("Chữ số lớn nhất trong tổng là:", max_cs)