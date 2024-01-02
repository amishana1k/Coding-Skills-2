from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, n: List[int]) -> List[int]:
        c_dict = Counter(n)
        result = []

        for value, count in c_dict.items():
            if count > len(n) / 3:
                result.append(value)

        return result
