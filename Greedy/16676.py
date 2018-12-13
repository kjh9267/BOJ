import sys

N = int(sys.stdin.readline())

if N < 11:
    print(1)
elif N < 111:
    print(2)
elif N < 1111:
    print(3)
elif N < 11111:
    print(4)
elif N < 111111:
    print(5)
elif N < 1111111:
    print(6)
elif N < 11111111:
    print(7)
elif N < 111111111:
    print(8)
else:
    print(9)