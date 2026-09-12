n=int(input())

matrix=[]

for i in range(n):
    elem=[int(num) for num in input().split()]
    matrix.append(elem)

flag=True

for i in range(n):
    for j in range(n):
        if j+1 not in matrix[i]:
            flag=False
    if not flag:
        break

matrix_new=[]

if flag:
    for i in range(n):
        elem=[]
        for j in range(n):
            elem.append(matrix[j][i])
        matrix_new.append(elem)
    for i in range(n):
        for j in range(n):
            if j+1 not in matrix_new[i]:
                flag=False
        if not flag:
            break

if flag:
    print('YES')
else:
    print('NO')