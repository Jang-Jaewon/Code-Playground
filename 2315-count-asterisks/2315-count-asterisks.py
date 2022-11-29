class Solution:
    def countAsterisks(self, s: str) -> int:
        l=[] 
        for i in s: 
            if '|' not in l: 
                l.append(i) 
            elif '|' in l and i=='|': 
                l.pop() 
        return l.count('*')