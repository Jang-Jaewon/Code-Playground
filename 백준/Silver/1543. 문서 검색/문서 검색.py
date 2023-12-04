data = input()
target = input()

index = 0
res = 0

while len(data) - index >= len(target):
    if data[index:index+len(target)] == target:
        res += 1
        index += len(target)
    else:
        index += 1

print(res)