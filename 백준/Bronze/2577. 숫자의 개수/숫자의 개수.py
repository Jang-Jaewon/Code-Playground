a = int(input())
b = int(input())
c = int(input())
res = a * b * c
res_list = list(str(res))
for i in range(10):
    num_ctn = res_list.count(str(i))
    print(num_ctn)