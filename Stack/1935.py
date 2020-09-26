# https://www.acmicpc.net/problem/1935

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    formula = input().rstrip()
    stack = list()
    operations = {'-', '+', '*', '/'}
    nums = [input().rstrip() for _ in range(N)]

    for value in formula:
        if value not in operations:
            stack.append(nums[ord(value) - 65])
            continue
        second = stack.pop()
        first = stack.pop()
        stack.append(str(eval(first + value + second)))

    print('{:.2f}'.format(float(stack[0])))