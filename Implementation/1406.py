# https://www.acmicpc.net/problem/1406

from collections import deque

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    left = deque(input().rstrip())
    right = deque()
    for _ in range(int(input())):
        cmd = input().split()
        try:
            if cmd[0] == 'L':
                right.appendleft(left.pop())
            elif cmd[0] == 'D':
                left.append(right.popleft())
            elif cmd[0] == 'B':
                left.pop()
            else:
                left.append(cmd[1])
        except IndexError:
            pass
    print(''.join(left),''.join(right), sep='')