from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(zip(indices,s))
        arr.sort()
        p,q = zip(*arr)
        return ''.join(q)
