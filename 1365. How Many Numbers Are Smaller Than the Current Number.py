from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out =[]
        for i in nums:
            count = len([x for x in nums if x < i])
            out.append(count)
        return out