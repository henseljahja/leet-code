from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(nums)-1,2):
            for j in range(nums[i]):
                arr.append(nums[i+1])
        return arr


