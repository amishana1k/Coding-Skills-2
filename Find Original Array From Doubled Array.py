#Find Original Array From Doubled Array

class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        n = len(changed)
        a = n // 2
        res = []
        
        for i in range(a):
            if a < n and (changed[i] * 2) == changed[a]:
                res.append(changed[i])
                a += 1
            else:
                return []

        return res
