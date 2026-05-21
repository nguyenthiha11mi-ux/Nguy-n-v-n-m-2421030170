

print("=== BT4 - TRA CUU DAN TOC ===")
dan_toc = {
    1: "Kinh",
    2: "Tay",
    3: "Nung",
    4: "Thai",
    5: "Kho me"
}

print("Bang ma dan toc:")
for ma, ten in dan_toc.items():
    print(f"  {ma} - {ten}")

ma = int(input("Nhap ma dan toc (1-5): "))
if ma in dan_toc:
    print("Dan toc:", dan_toc[ma])
else:
    print("Ma dan toc khong hop le")
