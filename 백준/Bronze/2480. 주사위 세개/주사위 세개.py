import sys
a=list(map(int,sys.stdin.readline().split()))
a.sort()
d=[0 for _ in range(7)]

for i in a:
    d[i]+=1

if max(d)==3:
    print(10000+d.index(max(d))*1000)
elif max(d)==2:
    print(1000+d.index(max(d))*100)
else:
    print(a[-1]*100)