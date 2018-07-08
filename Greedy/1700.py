import sys


n, k = map(int,sys.stdin.readline().split())
schedule = sys.stdin.readline().split()
plug = list()
cnt = 0
result = 0

if n >= k:
    print(0)
    exit()

for i in range(k):
    if len(plug) is n and i + 1 < k and schedule[i+1] not in plug:
        cnt += 1
        break
    if schedule[i] not in plug:
        plug.append(schedule[i])
        cnt += 1

for i in range(cnt-1,k):
    key = False
    if schedule[i] in plug:
        continue
    else:
        for u, j in enumerate(plug):
            if j not in set(schedule[i:k]):
                plug[u] = schedule[i]
                result += 1
                key = True
                break
        if key:
            continue
        for j in range(k-1,i-1,-1):
            if schedule[j] in plug:
                plug[plug.index(schedule[j])] = schedule[i]
                result += 1
                break

print(result)