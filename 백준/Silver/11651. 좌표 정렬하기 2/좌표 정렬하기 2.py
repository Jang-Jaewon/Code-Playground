n = int(input())
l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append((x,y))
l = sorted(l, key = lambda x: (x[1], x[0]))
for i in l:
    print(i[0], i[1])
