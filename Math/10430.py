import sys

a, b, c = map(int,sys.stdin.readline().split())

print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)

'''
(a+b)%c = (a%c + b%c)%c
(a*b)%c = (a%c * b%c)%c
a + b 또는 a * b의 크기가 너무 클 때 사용
'''