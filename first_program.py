n,m=[int(i) for i in input().split()]

matrix=[[0]*m for _ in range(n)]

counter=1

for i in range(n):
    for j in range(m):
        if i<=j:
            matrix[i][j]=counter
            counter+=1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()