class Solution:
    def sortSentence(self, s: str) -> str:
        l = [i[-1] + i[:-1] for i in s.split()]  
        l.sort()
        
        res = ""
        for i in l:
            res += i[1:] + ' '
        
        return res[:-1]