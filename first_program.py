n=int(input())

schoolchilds=[tuple(input().split()) for _ in range(n)]

for child in schoolchilds:
    print(*child)

print()

for name, mark in schoolchilds:
    if int(mark)>=4:
        print(name,mark)