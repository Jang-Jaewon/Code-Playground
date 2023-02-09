class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for i in list(str(num)):
            if not num % int(i):
                res += 1

        return res