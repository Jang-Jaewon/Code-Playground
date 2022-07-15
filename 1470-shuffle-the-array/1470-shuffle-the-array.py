class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [nums[i//2 + n*(i%2)] for i in range(0, 2*n)]
        return res
            