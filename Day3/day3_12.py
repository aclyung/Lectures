import random

numbers = []
for num in range(0, 10):
    numbers.append(random.randrange(0, 10))

print(numbers)

for num in range(0, 10):
    if num not in numbers:
        print("%d는(은) 리스트에 없습니다" % num)
