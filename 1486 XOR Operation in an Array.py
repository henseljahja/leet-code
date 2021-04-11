class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2*x for x in range(n)]
        out = 0
        for i in nums:
            out ^= i
        return out