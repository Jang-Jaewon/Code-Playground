def d(n):
  a = 0
  for x in list(str(n)):
    a = a + int(x)
  return n + a
a = []
for i in range(1,10001):
  k = d(i)
  a.append(k)
for b in range(1,10001):
  if b in a:
    pass
  else:
    print(b)