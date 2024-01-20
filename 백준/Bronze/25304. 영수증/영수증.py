total_price = int(input())
total_count = int(input())

calculate_price = 0
for i in range(total_count):
    value, count = map(int, input().split())
    calculate_price += value * count

if total_price == calculate_price:
  print("Yes")
else:
  print("No")