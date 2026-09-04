n,m=[int(i) for i in input().split()]

matrix_A=[]

for i in range(n):
    elem=[int(num) for num in input().split()]
    matrix_A.append(elem)

input()

m,k=[int(i) for i in input().split()]

matrix_B=[]

for i in range(m):
    elem=[int(num) for num in input().split()]
    matrix_B.append(elem)

matrix_result=[[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        elem=0
        for h in range(m):
            elem+=matrix_A[i][h]*matrix_B[h][j]
        matrix_result[i][j]=elem
print()

for i in range(n):
    print(*matrix_result[i])