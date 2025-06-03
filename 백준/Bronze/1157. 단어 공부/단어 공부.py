a = input()
a = a.upper()
d=[0 for _ in range(26)]
for i in a:
    d[ord(i)-65]+=1

max_alp = max(d)
if d.count(max_alp)>=2:
    print('?')
else:
    print(chr(d.index(max(d))+65))