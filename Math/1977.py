import math
m = input()
n = input()
sum = 0
list = []
for i in range(m,n+1):
    if int(math.sqrt(i))**2 == i:
        sum += i
        list.append(i)
if len(list) == 0:
    print -1
else:
    print sum
    print min(list)