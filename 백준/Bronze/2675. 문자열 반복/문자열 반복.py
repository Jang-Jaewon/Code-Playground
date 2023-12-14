amount = int(input())
for _ in range(amount):
  a,b = input().split()
  b = list(b)
  word = ''
  for i in b:
    word = word + i * int(a)
  print(word)