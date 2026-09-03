k = int(input())
s = input()

s_new = ""

for i in s:
    if i.isalpha() and i.islower():
        if 97 <= ord(i) + k <= 122:
            s_new += chr(ord(i) + k)
        else:
            s_new += chr(ord(i) + k - 26)
    elif i.isalpha() and i.isupper():
        if 65 <= ord(i) + k <= 90:
            s_new += chr(ord(i) + k)
        else:
            s_new += chr(ord(i) + k - 26)
    else:
        s_new += i

print(s_new)
