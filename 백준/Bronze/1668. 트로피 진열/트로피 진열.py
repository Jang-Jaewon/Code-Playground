import sys

def ascending(l):
    point = l[0]
    res = 1
    for i in range(1, len(l)):
        if point < l[i]:
            res += 1
            point = l[i]
    return res

n = int(sys.stdin.readline())
l = []
for i in range(n):
    height = int(sys.stdin.readline())
    l.append(height)    

print(ascending(l))
l.reverse()
print(ascending(l))