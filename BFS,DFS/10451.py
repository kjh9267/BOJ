import sys

for i in range(int(sys.stdin.readline())):
    n = input()
    a = range(1,n+1)
    b = map(int,raw_input().split())
    visit = []
    cnt = 0
    for j in range(n):
        if a[j] not in visit:
            queue = [a[j]]
            while len(queue) is not 0:
                x = queue.pop(0)
                visit.append(x)
                if b[a.index(x)] not in visit:
                    queue.append(b[a.index(x)])
            cnt += 1
    print cnt