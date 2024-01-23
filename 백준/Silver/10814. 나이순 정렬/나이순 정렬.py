n = int(input())
l = list()
for i in range(n):
    age, name = input().split()
    l.append((int(age), name))
l = sorted(l, key=lambda x: x[0])
for i in l:
    print(i[0], i[1])