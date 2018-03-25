import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().rstrip()
    x = command[:3]
    if x == 'pus':
        queue.append(int(command.split()[-1]))
    elif x == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif x == 'siz':
        print(len(queue))
    elif x == 'emp':
        if queue:
            print(0)
        else:
            print(1)
    elif x == 'fro':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)