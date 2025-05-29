import sys
h,m = map(int,sys.stdin.readline().split())
a=int(sys.stdin.readline())

h+=((m+a)//60)
m=((m+a)%60)

if h>=24:
    h-=24
print(h,m)