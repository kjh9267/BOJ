# https://www.acmicpc.net/problem/1111


def can_find_formula():
    if N == 1:
        return False
    if N == 2 and nums[0] != nums[1]:
        return False
    return True


def find_formula():
    x = nums[1] - nums[0]
    y = nums[2] - nums[1]

    if x != 0:
        a = y // x
    else:
        a = 0

    b = nums[1] - a * nums[0]

    return a, b


def is_correct_formula():
    for index in range(1, N):
        if nums[index] != nums[index - 1] * a + b:
            return False
    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))

    if not can_find_formula():
        print('A')
    elif N == 2:
        print(nums[0])
    else:
        a, b = find_formula()
        if is_correct_formula():
            print(a * nums[-1] + b)
        else:
            print('B')