while True:
    a, b = int(input("첫 번째 수를 입력: ")), int(input("첫 번째 수를 입력: "))
    oper = input("계산할 연산자(+,-,*,/):")
    if oper == '+':
        print("%d + %d = %d " % (a, b, a+b))
    elif oper == '-':
        print("%d - %d = %d " % (a, b, a-b))
    elif oper == '*':
        print("%d * %d = %d " % (a, b, a*b))
    elif oper == '/':
        print("%d / %d = %d " % (a, b, a/b))
    if input("Continue?(y or n): ") == "n":
        exit(0)
