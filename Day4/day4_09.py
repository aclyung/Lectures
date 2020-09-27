# a, b, c, d = 0, 0, 0, 0
# a = int(input("첫 번째 숫자: "))
# b = int(input("두 번째 숫자: "))
# c = int(input("세 번째 숫자: "))
# d = int(input("네 번째 숫자: "))
# print(a+b+c+d)
aa = [int(input("%d번째 숫자: " % (i+1))) for i in range(4)]
a = 0
a
for i in range(len(aa)):
    a += aa[i]
print(a)
