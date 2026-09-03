n=int(input())

holodilniki=[]
holodilniki_isalpha=[]


for i in range(n):
    holodilniki.append(input())
    if holodilniki[i].isalpha():
        holodilniki_isalpha.append(holodilniki[i])
    else:
        for i in range(len(holodilniki[i])):
            