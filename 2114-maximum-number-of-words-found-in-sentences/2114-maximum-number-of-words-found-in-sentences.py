class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(list(map(lambda x: len(x.split()), sentences)))