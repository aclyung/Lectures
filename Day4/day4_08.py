for i in range(9):
    if i < 5:
        a = 0
        print("  "*(4-i), end="")
        print("\u2605"*(2*i+1))
    else:
        print("  "*(i-4), end="")
        print("\u2605"*(2*(9-i)-1))
print("")

for i in range(9):
    if i < 5:
        k = 0
        while k < 4-i:
            print("  ", end="")
            k += 1
        k = 0
        while k < 2*i + 1:
            print("\u2606", end="")
            k += 1
        print("")
    else:
        k = 0
        while k < i-4:
            print("  ", end="")
            k += 1
        k = 0
        while k < 2*(9-i)-1:
            print("\u2606", end="")
            k += 1
        print("")
