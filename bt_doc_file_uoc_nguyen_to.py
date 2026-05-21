

print("BT DOC FILE - UOC SO NGUYEN TO ")

def uoc_so_nguyen_to(n):
    uoc = []
    for i in range(2, n):
        if n % i == 0:
            la_nto = True
            for j in range(2, i):
                if i % j == 0:
                    la_nto = False
                    break
            if la_nto:
                uoc.append(i)
    return uoc

# Tao file Input.txt mau
with open("Input.txt", "w") as f:
    f.write("12\n18\n30\n7\n")
print("Da tao Input.txt mau")

# Doc Input.txt, xu ly, ghi Output.txt
with open("Input.txt", "r") as f_in:
    with open("Output.txt", "w") as f_out:
        for dong in f_in:
            n = int(dong.strip())
            uoc = uoc_so_nguyen_to(n)
            f_out.write(str(uoc) + "\n")
            print(f"Uoc so nguyen to cua {n}: {uoc}")

print("Da ghi ket qua vao Output.txt")
