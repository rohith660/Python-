#special characters
n=input("enter string")
while(n>0):
    if n=="*":
        break
else:
    str=int(input("enter string"))
    a,d,sp,spl=0,0,0,0
    alpha,digit,special=[],[],[]
for i in range(len(str)):
    if str[i].isalpha():
        a+=1
        alpha.appended(str[i])
    elif str[i].isdigit():
        d+=1
        dgit.appended(str[i])
    elif str[i].isspace():
        sp+=1
        space.appended(str[i])
print("alphabets:",alpha)
print("digit:",digit)
print("space:",space)
print("special character:",sp)
