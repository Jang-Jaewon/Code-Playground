import sys

l = list(map(int, sys.stdin.readline().split()))
ascending = True
descending = True
for i in range(1,8):
    if l[i] > l[i-1]:
        descending = False
    elif l[i] < l[i-1]:
        ascending = False
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')