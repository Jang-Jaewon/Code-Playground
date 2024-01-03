import copy
def func(array, n):
    if len(array) == n:
        operations_list.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    func(array, n)
    array.pop()
    
    array.append('+')
    func(array, n)
    array.pop()
    
    array.append('-')
    func(array, n)
    array.pop()

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    operations_list = []
    func([], n-1)

    nums = [i for i in range(1, n+1)]

    for operations in operations_list:
        string = ""
        for i in range(n-1):
            string += str(nums[i]) + operations[i]
        string += str(nums[-1])
        res = eval(string.replace(" ", ""))
        if res == 0:
            print(string)
    print() 