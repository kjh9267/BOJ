# https://www.acmicpc.net/problem/3986

if __name__ =='__main__':
    input = __import__('sys').stdin.readline

    N = int(input())
    cnt = 0

    for _ in range(N):
        word = input().rstrip()
        stack = __import__('collections').deque()

        for idx, char in enumerate(word):
            if stack:
                if char == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        if not stack:
            cnt += 1
    print(cnt)