class Solution:
    def rotate(self, n: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(n)
        k = k % length  
        n.reverse()
        self.reverse_sublist(n, 0, k - 1)
        self.reverse_sublist(n, k, length - 1)
    def reverse_sublist(self, n: List[int], start: int, end: int) -> None:
        while start < end:
            n[start], n[end] = n[end], n[start]
            start += 1
            end -= 1
