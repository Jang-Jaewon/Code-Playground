class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = str(abs(x))[::-1]
        return int(reverse_x) == x
        