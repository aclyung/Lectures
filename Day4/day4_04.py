while True:
    try:
        a, b = int(input("첫 번째 수를 입력: ")), int(input("첫 번째 수를 입력: "))
    except Exception as e:
        print("exception caused")
        continue
    print(a+b)
