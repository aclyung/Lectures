weight = int(input("몸무게(kg): "))
height = int(input("키(cm): "))
print("BMI는 %.2f (kg/m^2) 입니다" %(weight/((height/100)**2)))