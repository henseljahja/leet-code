class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        sizeReq = int(len(A)/2)
        for i in A:
            if A.count(i) == sizeReq:
                return i
