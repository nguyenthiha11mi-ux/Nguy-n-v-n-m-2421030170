a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

temp = b
min_cs = 9

while temp > 0:
    cs = temp % 10
    
    if cs < min_cs and cs != 0:
        min_cs = cs
        
    temp = temp // 10

print("Chữ số nhỏ nhất của b là:", min_cs)

if a % min_cs == 0:
    print(a, "chia hết cho", min_cs)
else:
    print(a, "không chia hết cho", min_cs)