class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = 1
        num_list = list(map(int, str(n)))
        for num in num_list:
            res *= num
        return res - sum(num_list)