while 1:
    a = int(input("점수 입력: "))

    if a >= 90:
        print("A+" if a == 100 else "A")
    elif a >= 80:
        print("B")
    elif a >= 70:
        print("C")
    elif a >= 60:
        print("D")
    elif a >= 50:
        print("E")
    else:
        print("F")
