"""coins=[500, 100, 50, 10]
Money = int(input("구하려는 돈:"))
numb = 0 

for a in coins:
    numb+=Money//a
    print(str(a)+"원짜리 "+str(Money//a)+"개")
    Money %=a

print("총 동전갯수:"+str(numb)+"개\n바꾸지못한 잔돈:" + str(Money))"""

c500, c100, c50, c10, money = 0, 0, 0, 0, int(input("바꾸려는돈:"))
c500 = money//500
print("500원짜리 "+str(c500)+"개")
money%=500
c100 = money//100
print("100원짜리 "+str(c100)+"개")
money%=100
c50 = money//50
print("50원짜리 "+str(c50)+"개")
money%=50
c10 = money//10
print("10원짜리 "+ str(c10)+"개")
money%=10
print("총 동전갯수: %d개\n바꾸지못한 잔돈: %d" %(c500+c100+c50+c10, money))
