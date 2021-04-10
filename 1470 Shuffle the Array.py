from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xlen = int(len(nums)/2)
        x = nums[:xlen]
        y = nums[xlen:]
        out = []
        for i in range(xlen):
            out.append(x[i])
            out.append(y[i])
        return out
           
