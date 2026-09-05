n=int(input())

matrix_A=[]                 # Постоянная матрица
matrix_result=[]            # Результат возведения в степень

for i in range(n):          
    elem=[int(num) for num in input().split()]
    matrix_A.append(elem)
    matrix_result.append(elem)

m=int(input())

for _ in range(m-1):            # степень, в которую нужно возвести
    matrix_intermediate=[[0]*n for _ in range(n)]      # Промежуточная матрица
    for i in range(n):          # идем по строкам постоянной матрицы А
        for j in range(n):      # идем по столбцам матрицы intermediate
            elem=0
            for h in range(n):  #идем по каждому элементу и строки матрицы А и столбца матрицы intermediate
                elem+=matrix_A[i][h]*matrix_result[h][j]
            matrix_intermediate[i][j]=elem
    matrix_result=matrix_intermediate    # присваиваем конечной матрице промежуточный результат итеррации
print()

for i in range(n):
    print(*matrix_result[i])