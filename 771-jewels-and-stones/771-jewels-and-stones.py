class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for jewel in list(jewels):
            res += stones.count(jewel)
        return res
            