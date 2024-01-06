class Solution:
    def strStr(self, h: str, n: str) -> int:
        c=0
        for i in h:
            if n in h:
                return c
            else:
                c+=1
        else:
            return -1
