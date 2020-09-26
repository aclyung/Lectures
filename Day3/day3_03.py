Money_input = int(input("투입한돈: "))
price = int(input("물건의 값(단위: 100원단위): "))
change = Money_input - price

print("거스름돈:", change)
m500 = change//500
change = change%500
print("500원 짜리 %d개" %m500)
m100 = change//100
change = change%100
print("100원 짜리 %d개" %m100)


