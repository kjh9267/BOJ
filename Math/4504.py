import sys
n = int(sys.stdin.readline())
while True:
    a = int(sys.stdin.readline())
    if a is 0:
        break
    if a%n is 0:
        print '{} is a multiple of {}.'.format(a,n)
    else:
        print '{} is NOT a multiple of {}.'.format(a,n)