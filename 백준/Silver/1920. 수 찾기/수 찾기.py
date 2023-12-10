num1 = int(input())
l_1 = set(map(int, input().split()))
num2 = int(input())
l_2 = list(map(int, input().split()))

for i in l_2:
    if i not in l_1:
        print('0')
    else:
        print('1')