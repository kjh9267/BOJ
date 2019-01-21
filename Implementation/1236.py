#  성 지키기
#  https://www.acmicpc.net/problem/1236

input = __import__('sys').stdin.readline

if __name__ == '__main__':

    n, m = map(int,input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    row = [False for _ in range(n)]
    col = [False for _ in range(m)]
    result = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'X':
                row[i] = True
                col[j] = True

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                if row[i] is False and col[j] is False:
                    graph[i][j] = 'X'
                    row[i] = True
                    col[j] = True
                    result += 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                if row[i] is False:
                    row[i] = True
                    result += 1
                elif col[j] is False:
                    col[j] = True
                    result += 1

    print(result)
