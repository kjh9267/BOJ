# https://www.acmicpc.net/problem/18111

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M, B = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    min_time = float('inf')
    max_height = 0

    for height in range(257):
        has_blocks = B
        low_blocks = 0
        time = 0

        for row in range(N):
            for col in range(M):
                value = grid[row][col]
                if value > height:
                    diff = value - height
                    has_blocks += diff
                    time += diff * 2
                elif value < height:
                    diff = height - value
                    low_blocks += diff
                    time += diff

        if has_blocks >= low_blocks and min_time >= time:
            min_time = time
            max_height = height

    print(min_time, max_height)