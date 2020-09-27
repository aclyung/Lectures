a = [2*i for i in range(1, 101)]
b = a[::-1]
c = []
print(a, "\n", b)
for i in range(len(a)):
    c.append(a[len(a)-1-i])
print(c)
