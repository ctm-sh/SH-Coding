import sys
n, m = map(int,sys.stdin.readline().split())
d = [i+1 for i in range(n)]
for q in range(m):
    i,j = map(int,sys.stdin.readline().split())

    d[i-1:j]=d[i-1:j][::-1]

for r in d:
    print(r,end=" ")