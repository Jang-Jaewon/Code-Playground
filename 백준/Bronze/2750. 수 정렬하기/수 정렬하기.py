import sys
n = int(sys.stdin.readline())
l = list()
for i in range(n):
    num = int(sys.stdin.readline())
    l.append(num)
l.sort()
for i in l:
    print(i)