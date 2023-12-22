num_list = list(input().split())
l = []
for i in range(len(num_list)):
  num = num_list[i][::-1]
  l.append(int(num))
print(max(l))