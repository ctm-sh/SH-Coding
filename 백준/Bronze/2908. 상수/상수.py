import sys
n, m = sys.stdin.readline().split()
n,m = int(n[::-1]), int(m[::-1])
print(max(n,m))