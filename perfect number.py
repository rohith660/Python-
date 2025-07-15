n=int(input("enter a integer:"))
for i in range(1,n):
    sum=0
    if n%i==0:
        sum+=i
if sum==n:
    print("its perfect")
else:
    print("not perfect")
        
