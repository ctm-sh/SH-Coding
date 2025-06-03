import sys
d = list(map(int,sys.stdin.readline().split()))
d_ans = [1,1,2,2,2,8]
for i in range(6):
    print(d_ans[i]-d[i], end=" ")