import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

for i in range(2,-1,-1):
    print(n*int(str(m)[i]))
print(n*m)