import sys
x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
total=0
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    total+=(a*b)

if x==total:
    print('Yes')
else:
    print('No')