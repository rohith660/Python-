#matrix transpose 
a=[[1,2],[3,2]]
result=[[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
            result[i][j] = a[j][i]
for r in result:
     print(r)
