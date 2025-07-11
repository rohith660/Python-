A = [[4,6,7,8],[3,7,2,7],[7,3,7,5]]
C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A)):
        C[i][j]=A[j][i]
for r in C:
    print(r)
