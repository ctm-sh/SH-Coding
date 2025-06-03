import sys
n, m = map(int,sys.stdin.readline().split())
d = [0 for _ in range(n)]
for q in range(m):
    i,j,k = map(int,sys.stdin.readline().split())
    for p in range(i-1,j):
        d[p]=k

for r in d:
    print(r,end=" ")
