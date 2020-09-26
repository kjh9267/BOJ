# https://www.acmicpc.net/problem/4949

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    bracket = {'(', ')', '[', ']'}

    while True:
        line = input().rstrip()
        if line == '.':
            break

        stack = list()

        for char in line:
            if char not in bracket:
                continue
            stack.append(char)
            if len(stack) >= 2 and char == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
            elif len(stack) >= 2 and char == ']' and stack[-2] == '[':
                stack.pop()
                stack.pop()

        if stack:
            print('no')
        else:
            print('yes')
