import sys


def change(now):
    if now is 0:
        return 1
    else:
        return 0


def move(now,time):
    for i in people[now]:
        if visit[i[1]] is 0 and i[0] <= time and len(ship) < m:
            ship.append(i)
    time += t
    for i in ship:
        res[i[1]] = time
        visit[i[1]] = 1
    ship.clear()
    return time


def wait(now,time):
    for i in people[now]:
        if visit[i[1]] is 1:
            continue
        elif i[0] >= time:
            return i[0] - time
        else:
            return 0
    return float('inf')


m, t, n = map(int,sys.stdin.readline().split())
now = 0
people = [[],[]]
ship = []
visit = [0 for _ in range(n)]
res = [0 for _ in range(n)]
time = 0

for i in range(n):
    a, b = sys.stdin.readline().split()
    a = int(a)
    if b == 'left':
        people[0].append((a,i))
    else:
        people[1].append((a,i))

people[0] = sorted(people[0])
people[1] = sorted(people[1])

while 0 in visit:
    x = wait(0,time)
    y = wait(1,time)
    z = min(x,y)
    if x == y:
        time += x
        time = move(now,time)
        now = change(now)
    else:
        time += z
        time = move(now,time)
        now = change(now)
for i in res:
    print(i)