

print("=== BT1 - XU LY XAU KI TU ===")
xau = input("Nhap xau ki tu (12 ki tu): ")

if len(xau) != 12:
    print("Xau phai co dung 12 ki tu!")
else:
    print("Ki tu thu 3:", xau[2])
    print("Ki tu thu 4 den 7:", xau[3:7])
    print("Ki tu thu 11:", xau[10])
    print("Het xau:", xau[11])
