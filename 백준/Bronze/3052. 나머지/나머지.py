tail_list = []
for i in range(10):
    num = int(input())
    tail_list.append(num % 42)
print(len(set(tail_list)))