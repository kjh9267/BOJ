import sys
from collections import deque


n, k = map(int,sys.stdin.readline().split())
schedule = deque(sys.stdin.readline().split())
plug = list()
cnt = 0

while schedule:
    nxt = schedule.popleft()
    if len(plug) < n and nxt not in plug:
        plug.append(nxt)
    elif nxt in plug:
        continue
    else:
        for i in plug:
            if i not in schedule:
                plug.remove(i)
                plug.append(nxt)
                cnt += 1
                break
        else:
            temp = -1
            for i in set(plug):
                for j, u in enumerate(schedule):
                    if i == u:
                        if temp < j:
                            temp = j
                        break
            plug.remove(schedule[temp])
            plug.append(nxt)
            cnt += 1
print(cnt)