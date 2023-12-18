import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
res = 0
length = len(l)

count = 0
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j + 1, length):
            sum_value = l[i] + l[j] + l[k]
            if sum_value <= m:
                res  = max(res, sum_value)
print(res)
