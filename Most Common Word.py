class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        string = re.sub(r"[^a-zA-Z]", ' ', string).lower()
        freq = Counter(string.split())
        for x in banned:
            if x in freq:
                freq.pop(x)
            
        return max(freq, key=freq.get)
