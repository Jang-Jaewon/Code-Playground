import sys
from queue import deque
def queue_push(q, value):
    q.append(value)
def queue_pop(q):
    front = q.popleft()
    return front
n, k = list(map(int, sys.stdin.readline().split()))
queue = deque()
for i in range(1,n+1):
    queue_push(queue, i)
res = []
while len(queue) != 0:
    for i in range(k-1):
        front = queue_pop(queue)
        queue_push(queue, front)
    res.append(queue_pop(queue))
print("<", ', '.join(str(i) for i in res), ">", sep="")