import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [map(int,sys.stdin.readline().split()) for i in range(n+2)]
    queue = [graph[0]]
    visit = []
    while len(queue) is not 0:
        x = queue.pop(0)
        visit.append(x)
        key = False
        for i in range(len(graph)):
            if abs(graph[i][0] - x[0]) + abs(graph[i][1] - x[1]) <= 1000:
                if graph[i] is graph[-1]:
                    print 'happy'
                    key = True
                    break
                if graph[i] not in visit and graph[i] not in queue:
                    queue.append(graph[i])
        if key is True:
            break
    else:
        print 'sad'