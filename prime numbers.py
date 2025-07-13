a = int(input("enter the number:"))
b = int(input("enter the number:"))
c,p = [],[]
for num in range(a,b+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                c.append(num)
                break
        else:
            p.append(num)
print("the prime number is:",p,len(p))
print("the composite number is:",c,len(c))
