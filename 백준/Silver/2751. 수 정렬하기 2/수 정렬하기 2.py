import sys
def merge(left, right):
    merged = list()
    l_point, r_point = 0, 0
    while len(left) > l_point and len(right) > r_point:
        if left[l_point] > right[r_point]:
            merged.append(right[r_point])
            r_point += 1
        else:
            merged.append(left[l_point])
            l_point += 1
    while len(left) > l_point:
        merged.append(left[l_point])
        l_point += 1
    while len(right) > r_point:
        merged.append(right[r_point])
        r_point += 1
    
    return merged

def merge_split(data):
    if len(data) <= 1: return data
    medium = int(len(data) / 2)
    left = merge_split(data[:medium])
    right = merge_split(data[medium:])
    return merge(left, right)

n = int(sys.stdin.readline())
l = list()
for _ in range(n):
    data = int(sys.stdin.readline())
    l.append(data)
res = merge_split(l)
for i in res:
    print(i)