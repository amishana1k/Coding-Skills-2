class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        if word:
            return len(word[-1])
