a = int(input("please enter a value for variable a:\n"))
b = int(input("please enter a value for variable b:\n"))
res = [a + b, a-b, a*b, a/b]
opr = ['+', '-', '*', '/']
for c,o in zip(res,opr):
    print(a,o,b,c)
