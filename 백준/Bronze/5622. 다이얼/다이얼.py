import sys
n = sys.stdin.readline().strip()
d=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
cnt=0
for i in n:
    for j in range(9):
        if i in d[j]:
            cnt+=j+3
            break
print(cnt)