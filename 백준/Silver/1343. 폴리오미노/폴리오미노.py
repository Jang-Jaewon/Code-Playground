def polyomino(data):
  data = data.replace("XXXX", "AAAA")
  data = data.replace("XX", "BB")

  if "X" in data:
    return -1
  else:
    return data

data = input()
print(polyomino(data))