def cs(n,start):
    if n==0:
        return 1
    cnt = 0

    for i in range(start,5):
        cnt+=cs(n-1,i)
    return cnt
def cvs(n):
    return cs(n,0)
n=int(input("enter a number:"))
print(cvs(n))
    
