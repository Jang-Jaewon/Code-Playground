def fibonacci(n):
    d = [0 for i in range(n+1)]
    d[0] = 0
    d[1] = 1
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]

n = int(input())
print(fibonacci(n))