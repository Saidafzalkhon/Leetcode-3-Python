s = input()
k = ""
l = list(' ')
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[j] not in k:
            k+=s[j]
        else:
            l.append(k)
            k = ''
            break
l.sort(key = len,reverse=True)
print((len(l[0]) if s != '' else 0))