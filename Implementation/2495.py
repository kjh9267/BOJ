import sys

for _ in range(3):
    s = list(sys.stdin.readline().rstrip())
    length = 1
    result = 1

    for i in range(7):
        temp = s[i]
        if s[i + 1] != temp:
            length = 1
        if s[i + 1] == s[i]:
            length += 1
            if length > result:
                result = length

    print(result)