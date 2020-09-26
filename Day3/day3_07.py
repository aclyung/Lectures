import datetime

now = datetime.datetime.now().year
print("올해는 %d년 입니다" % now)
age = int(input("올해로 몇살이십니까? "))
print("2050년에는 %d살이 되시는군요" % (age+2050 - now))
