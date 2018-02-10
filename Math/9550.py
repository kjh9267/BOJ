t = input()
for i in range(t):
   n, k = map(int,raw_input().split())
   print sum([y/k for y in map(int, raw_input().split())])