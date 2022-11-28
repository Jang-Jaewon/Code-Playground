class Solution:
    def maxDepth(self, s: str) -> int:
        r = 0
        cnt = 0
        for c in s:
            if c == ")":
                if cnt:
                    cnt -= 1
                    r = max(r, cnt + 1)
            elif c == "(":
                cnt += 1  
        return r
