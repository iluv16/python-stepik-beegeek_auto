n=int(input())
massiv=[input() for _ in range(n)]

counter_s=[]
counter=[]

for i in range(n):
    if massiv[i] in counter_s:
        counter[counter_s.index(massiv[i])]+=1
    else:
        counter_s.append(massiv[i])
        counter.append(1)

maximum=max(counter)

for i in range(len(counter)):
    if counter[i]==maximum:
        print(counter_s[i])

