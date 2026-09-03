#spisok=[int(n) for n in input().split()]

n=int(input())

result=[]
virus='anton'

for i in range(n):
    name=''
    anton=input()
    for j in anton:
        if j in virus:
            name+=j
    print(name)
    if virus == name:
        result.append(i+1)

print(*result)
