n=int(input())
massiv=[int(num) for num in input().split()]

sum_m=sum(massiv)

if sum_m%(n-1) != 0:        # не можем разделить без остатка, значит не можем составить множества с одинаковыми суммами
    print('NO')
else:
    target_amount=sum_m//(n-1)
    non_target_amount = [i for i in massiv if i != target_amount]
    if len(non_target_amount) == 2 and sum(non_target_amount) == target_amount:
        print("YES")
    else:
        print("NO")
