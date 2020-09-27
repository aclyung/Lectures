a = 0
b = 0
for i in range(1, 101):
    if i % 3 == 0:
        continue
    a += i

print(a)
