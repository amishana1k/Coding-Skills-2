class Solution:
    def findDisappearedNumbers(self, n: List[int]) -> List[int]:
        n = list(sorted(n))
        res = []
        for i in range(1,len(n)+1):
            if i not in n:
                res.append(i)

        return res
