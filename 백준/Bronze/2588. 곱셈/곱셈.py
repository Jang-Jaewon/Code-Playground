a = int(input())
b = int(input())

out_num1 = a * ((b  % 100) % 10)
out_num2 = a * ((b  % 100) // 10)
out_num3 = a * (b // 100)
res = a * b
print(out_num1, out_num2, out_num3, res, sep='\n')