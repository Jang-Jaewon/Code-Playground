import heapq
n = int(input())
heap = []

for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

res = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum_value = a + b
    res += sum_value
    heapq.heappush(heap, sum_value)

print(res)