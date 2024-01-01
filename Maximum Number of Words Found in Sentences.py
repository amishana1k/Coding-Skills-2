class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        max_length = 0

        for i in range(len(s)):
            if i + 1 < len(s):
                if len(s[i]) > len(s[i + 1]):
                    max_length = len(s[i].split())

        return max_length
