# https://www.acmicpc.net/problem/1966

if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    T = int(input())

    for _ in range(T):
        N, M = map(int,input().split())
        data = list(map(int,input().split()))
        queue = __import__('collections').deque()
        for i, j in enumerate(data):
            queue.append((i, j))
        data.sort()
        target = queue[M]
        cnt = 1
        while queue:
            idx, priority = queue.popleft()
            if priority >= data[-1]:
                if idx == M:
                    print(cnt)
                    break
                data.pop()
                cnt += 1
            else:
                queue.append((idx, priority))