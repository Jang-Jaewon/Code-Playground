class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        min_str, max_str = min(strs), max(strs)
        i = 0
        while i < len(min_str) and i < len(max_str) and min_str[i] == max_str[i]: 
            i += 1
        return min_str[:i]