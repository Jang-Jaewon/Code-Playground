num_len = int(input())
num_list = list(map(int, input().split()))
max_score = max(num_list)
sum = 0
for i in num_list:
  sum = sum + i/max_score*100
print(sum/len(num_list))