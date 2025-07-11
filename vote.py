#grade for marks
num1 = int(input("enter mark 1"))
num2 = int(input("enter mark 2"))
num3 = int(input("enter mark 3"))
num4 = int(input("enter mark 4"))
num5 = int(input("enter mark 5"))
avg = num1+num2+num3+num4+num5/4
if avg <=90 and avg>=80:
    print("the graded is A ")
elif avg <80 and avg>=70:
    print("the graded is b ")
elif avg <70 and avg>=60:
    print("the graded is c ")
elif avg <60 and avg>=50:
    print("the graded is d ")
elif avg <50 and avg>=40:
    print("the graded is e ")
else :
    print("the graded is f ")

 


