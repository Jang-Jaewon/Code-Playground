N = int(input())
for _ in range(N):
  score = list(map(int, input().split()))
  score = score[1:]
  average_score = sum(score) / len(score)
  student = 0
  for i in score:
    if i > average_score:
      student = student + 1
  result = student / len(score) * 100
  result = round(result,3)
  print('{:.3f}%'.format(result))