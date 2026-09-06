n,t=[int(i) for i in input().split()]

T=[int(num) for num in input().split()]

counter_line=[0]*(n+1)      # счет строк
counter_column=[0]*(n+1)    # счет столбцов
counter_diagonal_R=0        # счет главной диагонали
counter_diagonal_L=0        # счет побочной диагонали

flag=False

for k in range(t):
    a=T[k]

    line=(a-1)//n
    column=(a-1)%n

    counter_line[line]+=1
    counter_column[column]+=1

    if line==column:
      counter_diagonal_R+=1
    if line+column==n-1:
      counter_diagonal_L+=1
      
    if counter_line[line]==n or counter_column[column]==n or counter_diagonal_R==n or counter_diagonal_L==n:
        print(k+1)
        flag=True
        break
           
if not flag:
    print(-1)

