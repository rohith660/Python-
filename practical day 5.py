#replacing the average
'''import statistics
l=[1,2,3,-1,4,5]
a=statistics.mean(l)
print(a)
l[3]=a
l.sort()
print(l)'''

#operator function
s = "1+2-3*1+10**2"
a = eval(s)
print(a)

a="1+2-3*1+10**2"
operands=[]
operators=[]
for i in a:
    if i.isdigit():
        operands.append(int(i))
    else:
        operators.append(i)
print(operands)
print(operators)









