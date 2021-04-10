from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
    	out = []
    	c = 0
    	for i in nums:
    		c += i
    		out.append(c)
    	return out
