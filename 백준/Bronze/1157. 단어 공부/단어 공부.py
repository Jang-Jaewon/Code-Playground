word = input().upper()  
set_word = list(set(word))
count_list = []
for i in set_word:
  count = word.count(i)
  count_list.append(count)
if count_list.count(max(count_list)) > 1:
  print('?')
else:
  max_index = count_list.index(max(count_list))
  print(set_word[max_index])