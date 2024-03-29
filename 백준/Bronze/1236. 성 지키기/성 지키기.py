# BOJ 1236(성 지키기)

import sys

n, m = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    l.append(sys.stdin.readline().strip())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if l[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

column_count = 0
for j in range(m):
    if column[j] == 0:
        column_count += 1

print(max(row_count, column_count))

