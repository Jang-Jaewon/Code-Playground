class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, value in enumerate(nums):
            gist = target - value
            if gist in dic:
                return [idx, dic[gist]]
            else:
                dic[value] = idx
