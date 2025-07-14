a=int(input("enter a integer:"))
n=a//100
m=a%100
result=(n+m)**2
if result==a:
    print("tech")
else:
    print("not tech")
