class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        diff = max_candy - extraCandies
        res = [True if candy >= diff else False for candy in candies ]
        return res
    