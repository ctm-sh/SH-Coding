import sys
n, m = map(int,sys.stdin.readline().split())
d = [i for i in range(n+1)]
for q in range(m):
    i,j = map(int,sys.stdin.readline().split())
    d[0]=d[i]
    d[i]=d[j]
    d[j]=d[0]

for r in d[1:]:
    print(r,end=" ")