N = int(input())
for i in range(N):
  target = input()
  score = 0
  sum = 0
  for j in target:
    if j == 'O':
      score = score + 1
    else:
      score = 0
    sum = sum + score
  print(sum)