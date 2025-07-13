#matrix multiplication
a=[[2,3],[3,4]]
b=[[4,5],[5,6]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]=a[i][j]+b[i][j]
for r in c:
    print(r)
