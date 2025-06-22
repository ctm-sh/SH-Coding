import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    order= sys.stdin.readline().split()
    if int(order[0])==1:
        queue.append(int(order[1]))
    elif int(order[0])==2:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif int(order[0])==3:
        print(len(queue))
    elif int(order[0])==4:
        if not queue:
            print(1)
        else:
            print(0)
    elif int(order[0])==5:
        if queue:
            print(queue[-1])
        else:
            print(-1)