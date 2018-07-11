import sys
from collections import deque

graph = dict()
line = []
case = 0

while True:
    line.extend(list(map(int,sys.stdin.readline().split())))

    if line[-2:] == [-1,-1]:
        exit()

    if line[-2:] == [0,0]:
        key = False
        case += 1
        line = line[:-2]

        if not line:
            print("Case {} is a tree.".format(case))
            continue

        for i in range(0,len(line),2):
            if line[i] in graph.keys():
                graph[line[i]].append(line[i+1])
            else:
                graph[line[i]] = [line[i+1]]

        root = 0
        check = 0

        for i in graph.keys():
            if i not in line[1:len(line):2]:
                root += i
                check += 1

        if check != 1:
            print("Case {} is not a tree.".format(case))
            line.clear()
            graph.clear()
            continue

        queue = deque()
        queue.append(root)
        visit = dict()

        for i in graph.keys():
            visit[i] = False

        for i in graph.values():
            for j in i:
                visit[j] = False

        visit[root] = True

        while queue:
            current = queue.popleft()

            if current not in graph.keys():
                continue

            for i in graph[current]:
                if visit[i] is True:
                    key = True
                    break
                else:
                    queue.append(i)
                    visit[i] = True

        for i in visit.values():
            if i is False:
                key = True
                break

        if key:
            print("Case {} is not a tree.".format(case))
            line.clear()
            graph.clear()
            continue

        line.clear()
        graph.clear()
        print("Case {} is a tree.".format(case))