sum = 0
while True:
    a = int(input("첫번째 숫자:"))
    if a == 0:
        break
    b = int(input("두번째 숫자:"))
    print("%d + %d = %d" % (a, b, a+b))
