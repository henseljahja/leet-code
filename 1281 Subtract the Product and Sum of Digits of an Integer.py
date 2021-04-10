from typing import List

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = list(str(n))
        arr = [int(x) for x in s]
        SOD = sum(arr)
        POD = 1
        for i in arr:
            POD *= i
        return POD - SOD

