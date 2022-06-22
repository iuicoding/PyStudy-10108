kg=float(input("체중을 입력하시오(kg)"))
m=float(input("키를 입력하시오(cm)"))/100
bmi=kg/(m**2)
print("bmi 수치:",bmi)
if bmi>=30:
    print("비만")
elif bmi>=25:
    print("과체중")
elif bmi>=20:
    print("정상")
else:
    print("저체중")