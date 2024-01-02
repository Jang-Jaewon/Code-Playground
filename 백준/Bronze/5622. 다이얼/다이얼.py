alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
second = 0
for i in alpabet_list:
  for j in i:
    for k in word:
      if j == k:
        second = second + alpabet_list.index(i) + 3
print(second)