n = list(raw_input())
for i in range(len(n)):
    n[i] = int(n[i])
if len(n) > 1:
    if n[1] < 5:
        for i in range(len(n)-1):
            n[i+1] = 0
    else:
        n[0] += 1
        for i in range(len(n)-1):
            n[i+1] = 0
r = n[::-1]
r.append(0)
n = r[::-1]
if len(list(str(n[1]))) == 2:
    n[0] += 1
    n[1] = int(list(str(n[1]))[1])
for i in range(len(n)):
    n[i] = str(n[i])
if n[0] == '0':
    n.pop(0)
    print "".join(n)
else:
    print "".join(n)

'''
a=input()
t=1
while(a>t*10):
    a+=5*t
    t*=10
    a-=a%t
print a
'''