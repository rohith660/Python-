def major(A):
    can=None
    count=0
    for num in A:
        if count==0:
            can=num
            count=1
        elif num==can:
            count+=1
        else:
            count -=1
    return can
A=[2,1,2,1,4,3,2,5,4,2]
print (major(A))
